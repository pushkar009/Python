import datetime
import os
import time as t
import psutil
process = 0
x = datetime.datetime.now()

#set the desired date
y = datetime.datetime(2024, 9, 22)

def terminate(p):
    print("Terminating!")
    #kill the process and exit from program
    os.system(f'taskkill /F /IM {p} /T')
    exit()

def check_status():
    for proc in psutil.process_iter():
        #check for chrome.exe in list of processes
        if proc.name() == "chrome.exe" or proc.name() == "brave.exe":
            #if found chrome.exe assign pid and break for loop
            process = psutil.Process(proc.pid)
            break
    
    if process.is_running() and process.status() == psutil.STATUS_RUNNING:
        #if all good then proceed to end process
        terminate(process.pid)
    else:
        t.sleep(3)
        terminate()

def execut():
    #open pdf
    os.startfile("result.pdf")
    #print("chrome running..")
    #show pdf for 15 sec
    t.sleep(15)
    check_status()

#check if today is the date set for task
if x.date() == y.date():
    execut()
#if today is not date, exit from program
else:
    exit()
