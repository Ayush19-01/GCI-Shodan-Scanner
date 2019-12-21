import shodan
import requests
import os
import socket
def prRed(skk): return str("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): return str("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): return str("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m {}\033[00m" .format(skk)) 
print("Welcome to the Shodan Scanner")
key=""    #Enter your shodan API key before running this file
api=shodan.Shodan(key)
def getip():
    print()
    r=requests.get("https://ifconfig.me/ip")
    print("Your Ip Address :"+" "+ r.text)
    print()
def shodansearch():
	os.system('clear')
	word=input("Input your query to search : ")
	print("Press q to end")
	r=api.search(word)
	info=""
	for i in r['matches'] :
		if len(i["hostnames"])>0:
			host1=i['hostnames'][0]
		else:
			host1=" "
		info+='{:28}{:18}{:65}{} \n'.format(prRed(str(i['ip_str'])),prGreen(str(i['port'])),prCyan(str(i['isp'])),prPurple(str(host1)))
	print(info)
def hostscan():
	os.system('clear')
	ip1=input('Enter domain:')
	print(prYellow(ip1))
	ip2=socket.gethostbyname(ip1)
	r=api.host(ip2)
	output='Hostnames:              '
	for i in r['hostnames']:
		output += (i + " " +"\n")
	output +='City:                    {}\nCountry:                 {}\nOrganization:            {} \nNumber of open ports:    {} \nPorts:'.format(r['city'], r['country_name'], r['org'], len(r['ports']))
	for j in r['data']:
		if 'product' in i:
			p=str(j['product'])
		else:
			p=" "
		output+="                   "+str(j['port'])+"   "
	print(output)
while True:
    
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
