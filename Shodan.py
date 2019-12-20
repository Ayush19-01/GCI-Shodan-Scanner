import pydoc
import shodan
import requests
import os
import socket
from colorama import Fore, Back, Style
from termcolor import colored

key='p01uPcafWSzzcIJeeZFRhUwVsN4OaNIz'
api=shodan.Shodan(key)

def getip():
    print()
    r=requests.get("https://ifconfig.me/ip")
    print("Your Ip Address :"+" "+ r.text)
    print()
def shodansearch():
    os.system('cls')
    word=input("Input your query to search : ")
    r=api.search(word)
    info = ''
    for i in r['matches']:
        if len(i["hostnames"])>0:
            host1=i['hostnames'][0]
        else:
            host1=" "
        print()
        info+=colored(str(i['ip_str']),'red')+"       "+ colored(str(i['port']),"green") + "      "+ colored(str(i['isp']),'blue')+"        "+ colored(str(host1),'yellow')+ "\n"
    pydoc.pager(info)
def hostscan():
    os.system('cls')
    ip1=input('Enter domain:')
    ip2=socket.gethostbyname(ip1)
    r=api.host(ip2)
    output = "\033[0;32m" + ip1 + '\033[0m\nHostnames:              '
    for i in r['hostnames']:
        output += (i + " " +"\n")
        output +='City:                    {}\nCountry:                 {}\nOrganization:            {} \nNumber of open ports:    {} \nPorts:'.format(r['city'], r['country_name'], r['org'], len(r['ports']))
    for i in r['data']:
        if 'product' in i:
            p=str(i['product'])
        else:
            p=" "
        output+= ("    \033[1;34m{:<6}\033[0m  {}\n").format(str(i['port']), p)
    pydoc.pager(output)
while True:
    print("Welcome to the Shodan Scanner")
    print("""Choose from the following:\n1) Get Your IP\n2) Shodan search to scan Ip, port, host\n3) Scan a specific host\n4) Exit""")
    inp1=int(input("Shodan>"))
    if inp1==1:
        getip()
    elif inp1==2:
        shodansearch()
    elif inp1==3:
        hostscan()
    elif inp1>3:
        print("[+]Closing the program....")
        break
