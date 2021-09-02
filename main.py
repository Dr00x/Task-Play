import pyautogui as pg
import keyboard as kb
from time import sleep
from colorama import Fore, init

init(autoreset=True)
print(Fore.BLUE+"[1] To start Record, [2] To view Recorded keys, [3] to Play recorded keys Press and wait 5 second to start play, \n[clr] to clear all keys recorded. \nPress [2] while recording to break recording system. Dont Press the keys too fast or some keys is dont recorded")
print(Fore.GREEN+"How much you need to record?")

key = []
commandLine = ''
try: 
    ammount = int(input('>:'))
except:
    print(Fore.RED + "Error")
    exit()

loop = False

def getKey(time):
    for i in range(0,time):
        sleep(0.2)
        a = kb.read_key()
        if a != "2":
            print(Fore.YELLOW + f"{a}")
        key.append(a)

        if a == "2":
            key.remove(a)
            break

while True:
    commandLine = input('>:')
    if commandLine == "1":
        getKey(ammount)
    elif commandLine == "2":
        print(key)
    elif commandLine == "loop":
        loop = True
        print(Fore.YELLOW + "Loop is on")
    elif commandLine == "loopoff":
        loop = False
        print(Fore.YELLOW + "Loop is off")
    elif commandLine == "3":
        try:
            sleep(3)
            if loop == True:
                while True:
                    for i in key:
                        pg.press(i)
            else:
                for i in key:
                    pg.press(i)
        except:
            print(Fore.RED + "Error")
    elif commandLine == "clr":
        key.clear()
        

#  ____ _____  ____  ____ __  __
# | _) \| () )/ () \/ () \\ \/ /
# |____/|_|\_\\____/\____//_/\_\________
#dr00x_