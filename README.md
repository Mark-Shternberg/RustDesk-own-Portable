# RustDesk-own-Portable
Portable version of RustDesk installation with auto install self-hosted configuration (auto En/Rus)

This script will download portable version of RustDesk to desktop and automaticly create a file with a given server configuration
Этот скрипт скачает портативную версию RustDesk на рабочий стол и автоматически создаст файл с заданной конфигурацией сервера

------------------------------------------------------------

Before compiling the file, add a link to download the portable version of Rustdesk and enter the configuration of your server (there are comments in the code where you need to do it)
After that you can compile py file into exe:

pyinstaller.exe --windowed -F RustDesk-install.py

If you want to add icon to exe, download ico file to the same directory as py file and compile with:

pyinstaller.exe --windowed -F --icon=rd.ico --add-data "rd.ico;." RustDesk-install.py

------------------------------------------------------------

Перед компиляцией файла нужно добавить ссылку на скачивание портативной версии RustDesk и вписать конфигурацию своего сервера (в коде есть комментарии, где это нужно сделать)
После этого можно скомпилировать файл следующей командой:

pyinstaller.exe --windowed -F RustDesk-install.py

Если есть надобность добавить иконку дляустановщика, нужно скачать ico файл в ту же директорию с py файлом и выполнить следующую команду:

pyinstaller.exe --windowed -F --icon=rd.ico --add-data "rd.ico;." RustDesk-install.py
