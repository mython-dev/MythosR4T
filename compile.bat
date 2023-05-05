@echo off

pip install -r requirements.txt

pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --uac-admin --copy-metadata magic_filter --version-file "version.py" --add-data "libs;libs/" --add-data "logs;logs/" "MythosR4T.py"

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null