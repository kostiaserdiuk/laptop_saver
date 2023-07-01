import psutil as ps
import subprocess
from time import perf_counter
import win32api
import win32con
import configparser
import sys


config = configparser.ConfigParser()
config.read("config.ini")

gpu = config["GPU"]["PNPDeviceID"]
gpu_disable = config["GPU"]["gpu_mustbedisabled"]
saving_rate = config["Display"]["SavingRate"]
performance_rate = config["Display"]["PerformanceRate"]


plugged = ps.sensors_battery().power_plugged

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

if len(sys.argv) == 2 and sys.argv[1] == "-i":
        specs = subprocess.run(['powershell', '-command', "Get-CimInstance -ClassName win32_VideoController | Format-List -Property Name, Status, PNPDeviceID"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(specs.stdout.decode("utf-8"))
        exit()

if len(sys.argv) == 2 and sys.argv[1] == "-b":
    battery = ps.sensors_battery()
    print("Battery Percent: ", battery.percent)
    print("Battery remaining : ", convertTime(battery.secsleft))
    exit()


if plugged == False:
    if gpu_disable == "True" and gpu == "None":
        specs = subprocess.run(['powershell', '-command', "Get-CimInstance -ClassName win32_VideoController | Format-List -Property Name, Status, PNPDeviceID"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(specs.stdout.decode("utf-8"))
        exit()
    elif gpu_disable == "True" and gpu != "None":
        try:
            process = subprocess.run(["powershell",
                            "-command", 
                            f'pnputil /disable-device "{gpu}"'], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            err = process.stderr
            err = err.decode("utf-8")
            if err != "":
                print(err)
                exit()
        except:
            print("Invalid GPU PNPDeviceID")
            exit()
    if saving_rate != "None":
        if saving_rate == performance_rate:
            exit()
        else:
            try:
                saving_rate = int(saving_rate)
            except:
                print("Invalid saving rate")
                exit()
            dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
            if dm.DisplayFrequency == saving_rate:
                exit()
            dm.DisplayFrequency = saving_rate
            ret = win32api.ChangeDisplaySettings(dm, 0)
            if ret == 0:
                exit()
            else:
                if ret == win32con.DISP_CHANGE_BADDUALVIEW:
                    print("The settings change was unsuccessful because the system is DualView capable")
                elif ret == win32con.DISP_CHANGE_BADFLAGS:
                    print("An invalid set of flags was passed in.")
                elif ret == win32con.DISP_CHANGE_BADMODE:
                    print("The graphics mode is not supported.")
                elif ret == win32con.DISP_CHANGE_BADPARAM:
                    print("An invalid parameter was passed in. This can include an invalid flag or combination of flags.")
                else:
                    exit()
        
else:
    if gpu != "None":
        try:
            process = subprocess.run(["powershell",
                            "-command",
                            f'pnputil /enable-device "{gpu}"'], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            err = process.stderr
            err = err.decode("utf-8")
            if err != "":
                print(err)
                exit()
        except:
            print("Invalid GPU PNPDeviceID")
            exit()
    if performance_rate != "None":
            if saving_rate == performance_rate:
                exit()
            else:
                try:
                    performance_rate = int(performance_rate)
                except:
                    print("Invalid performance_rate rate")
                    exit()
                dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
                if dm.DisplayFrequency == performance_rate:
                    exit()
                dm.DisplayFrequency = performance_rate
                ret = win32api.ChangeDisplaySettings(dm, 0)
                if ret == 0:
                    exit()
                else:
                    if ret == win32con.DISP_CHANGE_BADDUALVIEW:
                        print("The settings change was unsuccessful because the system is DualView capable")
                    elif ret == win32con.DISP_CHANGE_BADFLAGS:
                        print("An invalid set of flags was passed in.")
                    elif ret == win32con.DISP_CHANGE_BADMODE:
                        print("The graphics mode is not supported.")
                    elif ret == win32con.DISP_CHANGE_BADPARAM:
                        print("An invalid parameter was passed in. This can include an invalid flag or combination of flags.")
                    else:
                        exit()