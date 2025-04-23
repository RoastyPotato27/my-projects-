# Atomation for closing WindHawk and opening VirtualBox >
import psutil, subprocess, time, os

# Terminate Windhawk >
def close_app(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == app_name:
            found = True
            try:
                proc.kill()
                print(f'{app_name} (PID {proc.pid}) Successfully Terminated.')
            except Exception as e:
                print(f"{app_name} (PID {proc.pid}) Could Not Terminate Properly: {e}")
                
    if not found:
        print(f"{app_name} Is Not Running.")
                
# Open VirtualBox >
def open_app(app_path):
    try:
        subprocess.Popen(app_path)
    except Exception as e:
        print(f"{app_path} Could Not Be Launched: {e}")
    
    
# MAIN FUNCTION >
if __name__ == '__main__':
    close_app('windhawk.exe') 
    time.sleep(5)
    open_app(r"C:\Program Files\Oracle\VirtualBox\VirtualBox.exe")