# GCI-Shodan-Scanner
Documentation of Shodan Scanner attacks

___Attack 1) IP Address:___

![alt text](https://github.com/Ayush19-01/GCI-Shodan-Scanner/blob/master/resources/Screenshot%20from%202019-12-20%2018-04-26.png)

_Code snippet used:_
```
def getip():
    print()
    r=requests.get("https://ifconfig.me/ip")
    print("Your Ip Address :"+" "+ r.text)
    print()
```    
___Attack 2) Shodan Search to scan IPs, Hostnames, ports :___

![alt text](https://github.com/Ayush19-01/GCI-Shodan-Scanner/blob/master/resources/Screenshot%20from%202019-12-20%2018-20-48.png)

_Code snippet used:_

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
___Attack 3) Scanning a specific Host :___

![alt text](https://github.com/Ayush19-01/GCI-Shodan-Scanner/blob/master/resources/Screenshot%20from%202019-12-20%2018-05-45.png)

_Code snippet used:_
        
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
## Made for GCI 2019 by Ayush19
