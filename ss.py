import os
import subprocess
import time
import shutil
def check_and_delete(file_path):
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)
def remove_theme():
    config_dirs = ['autostart', 'cairo-dock', 'dconf', 'gtk-3.0', 'Mousepad', 'pulse', 'Thunar', 'menu', 'ristretto', 'rofi', 'xfce4']
    for the_config_dir in config_dirs:
        check_and_delete(os.path.join("/data/data/com.termux/files/home/.config", the_config_dir))
def stop_darkos():
    os.system("box64 wineserver -k")
    os.system('pkill -f "app_process / com.termux.x11"')
    os.system('pkill -f pulseaudio')
    print("shutdown........")
    os.system("am startservice -a com.termux.service_stop com.termux/.app.TermuxService")
    os.system("pkill -f com.termux.x11")
    subprocess.run(['am', 'broadcast', '-a', 'com.termux.x11.ACTION_STOP', '-p', 'com.termux.x11'])
    os._exit(0)      
def check_current_theme():
    custom_theme = "/data/data/com.termux/files/usr/glibc/opt/darkos/custom_theme.txt"
    if os.path.isfile(custom_theme):
        with open(custom_theme, 'r') as f:
            theme_content = f.read()
            if theme_content == "android_theme":
                theme_path = "/data/data/com.termux/files/usr/glibc/opt/personalise/downlaod/android.tar.xz"
                if os.path.exists(theme_path):
                    remove_theme()
                    time.sleep(1)
                    os.system(f"tar -xJvf {theme_path} -C $HOME &>/dev/null")
                    time.sleep(1)
                    stop_darkos()                
            elif theme_content == "macos_theme":
                theme_path = "/data/data/com.termux/files/usr/glibc/opt/personalise/downlaod/macos.tar.xz"
                if os.path.exists(theme_path):
                    remove_theme()
                    time.sleep(1)
                    os.system(f"tar -xJvf {theme_path} -C $HOME &>/dev/null")
                    time.sleep(1)
                    stop_darkos()
            elif theme_content == "manjaro_theme":
                theme_path = "/data/data/com.termux/files/usr/glibc/opt/personalise/downlaod/manjaro.tar.xz"
                if os.path.exists(theme_path):
                    remove_theme()
                    time.sleep(1)
                    os.system(f"tar -xJvf {theme_path} -C $HOME &>/dev/null")
                    time.sleep(1)
                    stop_darkos()
            elif theme_content == "windows10_theme":
                theme_path = "/data/data/com.termux/files/usr/glibc/opt/personalise/downlaod/windows10.tar.xz"
                if os.path.exists(theme_path):
                    remove_theme()
                    time.sleep(1)
                    os.system(f"tar -xJvf {theme_path} -C $HOME &>/dev/null")
                    time.sleep(1)
                    stop_darkos()
            print("something went wrong (not readable)")
            print("please contact the developer (https://t.me/DARKOS4android/)")
            exit(0)  
    else:
        print("It looks like you have not installed any theme yet")
        print("Please install the themes first")
        exit(0)     
check_current_theme()    

