import os
from tkinter import *
from tkinter import ttk
from urllib import request
import sys
import locale

if ("Russian_Russia" in locale.getlocale()):
    lang = "rus"
else:
    lang = "eng"

isExist1 = os.path.exists(os.environ['USERPROFILE'] + '\Desktop\RustDesk.exe')
isExist2 = os.path.exists(r'C:\Users\Public\Desktop\RustDesk.exe')
isExist3 = os.path.exists(r'C:\Users\Public\Desktop\RustDesk.lnk')
isExist4 = os.path.exists(os.environ['USERPROFILE'] + '\AppData\Roaming\RustDesk\config\RustDesk2.toml')
isExist5 = os.path.exists(os.environ['USERPROFILE'] + '\AppData\Roaming\RustDesk\config')
isExist6 = os.path.exists(os.environ['USERPROFILE'] + '\AppData\Roaming\RustDesk')

#URL to download portable exe of RustDesk
url_exe = 'URL'

#Config of self-hosted server
config = 'rendezvous_server = \'example.com\'\n\
nat_type = 1\n\
serial = 0\n\n\
[options]\n\
allow-remote-config-modification = \'Y\'\n\
enable-audio = \'N\'\n\
custom-rendezvous-server = \'example.com\'\n\
relay-server = \'example.com\'\n\
api-server = \'https://example.com\'\n\
key = \'KEY\' \
'

path_exe = os.environ['USERPROFILE'] + "\\Desktop\\RustDesk.exe"
path_toml = os.environ['USERPROFILE'] + "\\AppData\\Roaming\\RustDesk\\config\\RustDesk2.toml"

def massage(title,error):
    massage = Tk()
    screen_width = massage.winfo_screenwidth()  # Width of the screen
    screen_height = massage.winfo_screenheight() # Height of the screen
    x = (screen_width/2) - (350/2)
    y = (screen_height/2) - (150/2)
    massage.geometry('%dx%d+%d+%d' % (350, 130, x, y))
    massage.iconbitmap(sys.executable)
    massage.title(title)

    Label(massage, text=error, font=('Helvetica 12 bold')).pack(pady=20)
    if (lang == 'rus'):
        button = 'ОК'
    else:
        button = 'OK'
    ttk.Button(massage, text=button, command= massage.destroy).pack()
    massage.mainloop()

if (isExist1) or (isExist2) or (isExist3) or (isExist4):
    if (lang == 'rus'):
        massage('Ошибка','RustDesk уже установлен\n в Вашей системе')
    else:
        massage('Error','RustDesk already installed')
else:
    if not (isExist6):
        os.mkdir(os.environ['USERPROFILE'] + "\\AppData\\Roaming\\RustDesk")
    if not (isExist5):
        os.mkdir(os.environ['USERPROFILE'] + "\\AppData\\Roaming\\RustDesk\\config")
    try:
        response = request.urlretrieve(url_exe, path_exe)
    except:
        if (lang == 'rus'):
            massage('Ошибка','RustDesk не удалось скачать')
        else:
            massage('Error','RustDesk downloading error')
        quit()
    try:
        f = open(path_toml, "x")
        f = open(path_toml, "w")
        f.write(config)
        f.close()
    except:
        if (lang == 'rus'):
            massage('Ошибка конфигурации','RustDesk установлен\nНо не удалось установить конфигурацию!')
        else:
            massage('Error','RustDesk installed\nBut without configuration!')
        quit()
    if (lang == 'rus'):
        massage('Успешно','RustDesk установлен\nИконка на рабочем столе')
    else:
        massage('Success','RustDesk installed\nIcon on the desktop')
