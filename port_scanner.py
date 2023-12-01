#In this Python file we're going to create a port scanner

#We start this project by importing all moudle that will be used in the python file

import pyfiglet #this is module to create fancy test with large fonts and sizes in the output 
import sys
import socket #used to communicate over the network
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER!")#using pyfiglet here to create the fancy text we commented at the beginning 
print(ascii_banner)

target=input(str("Target IP: ")) #input the ip you would like to be scanned

#Add Banner
print("_" * 50)
print("Scanning Target: "+ target)
print("Scanning started at: " +str(datetime.now()))
print("_" * 50)

try: 
    #we will scan ports between 1 to 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #retuns an error indicator 
        result = s.connect_ex((target,port))
        if result ==0:
            print('[*] {} is open'.format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting the program!")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit()
except socket.error:
    print("Server not responding!")
    sys.exit()
