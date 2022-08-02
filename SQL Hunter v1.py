#!/usr/bin/env python3

#   This script is made for penetration testing on a specific website only.
#   Please don't use it in an illegal way.
#   Instagram: @a7.acc    Telegram: @A7_acc


# Importing the necessary packages
try:
    from time import sleep
    import sys,platform
    import requests,threading, schedule
    from os import system
    from random import choice
    from colored import fg,attr
except ModuleNotFoundError as err:
    print('ERROR! > Please install this library: '+str(err.name))
    print('By writing: pip install '+str(err.name))
    sleep(5)
    sys.exit()

# Detecting the OS
ops_release = str(platform.release())
ops = str(platform.system())
if '2012ServerR2' not in ops_release and ops == 'Windows' or ops == 'Linux':
    g = lambda x : fg('green')+x+attr('reset')
    rod = lambda x : fg('red')+x+attr('reset')
    b = lambda x : fg('blue')+x+attr('reset')
    y = lambda x : fg('yellow')+x+attr('reset')
    c = lambda x : fg('cyan')+x+attr('reset')
    m = lambda x : fg('magenta')+x+attr('reset')
    clear = lambda: system("cls")
    if ops == 'Linux':
        clear = lambda: system("clear")
else:
    g = lambda x : x
    rod = lambda x : x
    b = lambda x : x
    y = lambda x : x
    c = lambda x : x
    m = lambda x : x
    clear = lambda: system("cls")


# Markers
exl = '['+rod('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+b('*')+']'
clear()

logo = rod('''
 _______  _______  _                            _       _________ _______  _______ 
(  ____ \(  ___  )( \        |\     /||\     /|( (    /|\__   __/(  ____ \(  ____ )
| (    \/| (   ) || (        | )   ( || )   ( ||  \  ( |   ) (   | (    \/| (    )|
| (_____ | |   | || |        | (___) || |   | ||   \ | |   | |   | (__    | (____)|
(_____  )| |   | || |        |  ___  || |   | || (\ \) |   | |   |  __)   |     __)
      ) || | /\| || |        | (   ) || |   | || | \   |   | |   | (      | (\ (   
/\____) || (_\ \ || (____/\  | )   ( || (___) || )  \  |   | |   | (____/\| ) \ \__
\_______)(____\/_)(_______/  |/     \|(_______)|/    )_)   )_(   (_______/|/   \__/
                                                                                   ''')+f'\n                                             CopyRight: {m("instagram.com/a7.acc")}\n'
print(logo)

print(exl+f' {rod("DISCLAIMER")}: Please only use this tool on websites pages that you have permission to test!')
print(mult+f" An example of a checkable page:   {g('http://www.example.org/article.php?id=9')}")
print(mult+f" An example of a UNcheckable page: {rod('http://example.org')}\n")

# TO GENERATE RANDOM USER AGENT
def generate_user_agent():
    useragents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2828.31 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.44 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2965.63 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.69 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.18 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)'
        'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2690.91 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2777.66 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2898.2 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2801.53 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)'
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2694.39 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2703.73 Safari/537.36'
        'Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; WOW64; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2800.88 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2646.45 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2646.73 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.49 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2834.2 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2833.13 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2799.34 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2845.18 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2889.10 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.89 Safari/537.36'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2770.77 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2760.44 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2751.15 Safari/537.36'
    ]
    return choice(useragents)

while True:
    print(mult+'       CHOOSE A MODE       ')
    print(f'[{g("1")}] Check pages\' vulnerability ')
    print(f'[{g("2")}] Check pages\' existence ')
    mode = input('--------------> ')
    if mode in '12':
        break
clear()

while True:
    print(f'[{b(str("1"))}] Manually enter sites file name\n[{b(str("2"))}] Default sites file name (sites.txt)')
    name = input('--------------> ')
    if name in '12':
        break

if name == '1':

    while True:
        global file
        try:
            file_name = input(ques+' Enter Your Sites File Name: \n--------------> ')
            if not file_name.endswith('.txt'):
                file_name += '.txt'
            # deepcode ignore PT: It's running on a local machine
            with open(file_name,'r',encoding='utf-8') as filee:
                file = filee.read().splitlines()
                break
                
        except:
            print(exl+' Could\'nt find the file: '+str(file_name))
            print(mult+' Make sure your file is in the same folder as the program!')
            sleep(2)
            clear()
elif name == '2':
    try:
        file1 = open('sites.txt','r',encoding='utf-8')
        file = file1.read().splitlines()
        file1.close()
    except Exception as e:
        print(exl+f' Error While Getting The File: {c("sites.txt")}')
        print(exl+' Error Message >> '+str(e))
        print(mult+f' Make sure the file {b("sites.txt")} is in the same folder as the program and try again!')
        sleep(4)
        sys.exit()


# To keep track of everything
bad = 0
good = 0
Not = 0
error = 0
counter = 0

# Most Common SQL Injection Errors
errors = ['mysql_fetch_array()','mysql_num_rows()','Error Occurred While Processing Request',"Server Error in'/'Application",'Microsoft OLE DB Provider for ODBC Drivers error','error in your SQL syntax','VBScript Runtime','ADODB.Field','BOF or EOF','ADODB.command','JET Database','Syntax error','mysql_fetch_row()','include()','mysql_fetch_assoc()','mysql_fetch_object()','mysql_numrows()','GetArray()','FetchRow()','Input string was not in a correct format','Microsoft VBScript;','Invalid Querystring','OLE DB Provider for ODBC']

# functions 
# mode 1 :: vulnerability checking
def vulnerability():
    global counter,bad,good,Not,error,file,proxies
    while True:
        if ops == 'Windows':
            system(f'title ALL:{str(counter)}/{str(len(file))}   GOOD:{str(good)}   BAD:{str(bad)}   ERROR:{str(error)}   UNCHECKABLE:{str(Not)}')
        else:
            sys.stdout.flush()
            print(f"\r{c('ALL')}:{str(counter)}/{str(len(file))}   {g('GOOD')}:{str(good)}   {rod('BAD')}:{str(bad)}   {y('ERROR')}:{str(error)}   {b('UNCHECKABLE')}:{str(Not)}",end=' ')
        try:
            site = file[counter]
            counter += 1
        except IndexError:
            break
        
        added = False
        if 'http://' or 'https://' in site:
            if '?' in site and '=' in site:
                try:
                    # deepcode ignore SSRF: It's running on a local machine
                    res = requests.get(str(site)+"'",headers={'user-agent':generate_user_agent()},proxies=choice(proxies),timeout=10)
                except:
                    error += 1
                    continue
                if res.ok:
                    for er in errors:
                        if er in res.text:
                            try:
                                # deepcode ignore SSRF: It's running on a local machine
                                res2 = requests.get(str(site),headers={'user-agent':generate_user_agent()},proxies=choice(proxies),timeout=10)
                                if er in res2.text:
                                    break
                            except:
                                pass
                            good += 1
                            added = True
                            print('\n===========================')
                            print(ha+' PAGE: '+g(str(site)))
                            print(ha+' ERROR:'+y(str(er)))
                            print('===========================')
                            with open('vulnerable_sites.txt','a', encoding='utf-8') as fill:
                                fill.write(site+'\n')
                            break
            else:
                added = True
                Not += 1
        else:
            added = True
            Not += 1
        if not added:
            bad += 1

# mode 2 :: existence checking
def existence():
    global counter,bad,good,error,file,proxies
    while True:
        if ops == 'Windows':
            system(f'title ALL:{str(counter)}/{str(len(file))}   GOOD:{str(good)}   BAD:{str(bad)}   ERROR:{str(error)}')
        else:
            sys.stdout.flush()
            print(f"\r{c('ALL')}:{str(counter)}/{str(len(file))}   {g('GOOD')}:{str(good)}   {rod('BAD')}:{str(bad)}   {y('ERROR')}:{str(error)}",end=' ')
        
        try:
            site = file[counter]
            counter += 1
        except IndexError:
            break
        if 'http://' in site or 'https://' in site:
            try:
                # deepcode ignore SSRF: It's running on a local machine
                res = requests.get(str(site),headers={'user-agent':generate_user_agent()},proxies=choice(proxies),timeout=10)
                if res.ok and res.status_code == 200:
                    good += 1
                    print(ha+' '+g(str(site)))
                    with open('exist_sites.txt','a', encoding='utf-8') as fill:
                            fill.write(site+'\n')
                else:
                    bad += 1
            except:
                error += 1

        else:
            bad += 1


# All proxies will be saved here
proxies = []

# Adding proxies
print(f"{rod('NOTE')}: The program doesn't need proxies to work, please only add proxies if you have good ones otherwise the program will skip a lot of pages and will be slow!")
proxy = input(ques+' Do you want to add proxies? (Y/N) >> ').lower()
if proxy == 'y':

    while True:
        try:
            proxies_file_name = input(ques+' Enter Your Proxies File Name: \n--------------> ')
            if not proxies_file_name.endswith('.txt'):
                proxies_file_name += '.txt'
            # deepcode ignore PT: It's running on a local machine
            with open(proxies_file_name,'r') as pr:
                proxies_a = pr.read().splitlines()
            break
        except Exception as ee:
            print(exl+' Error while openning proxies file: '+y(str(ee)))
            print(mult+f' Make sure the file {b(proxies_file_name)} is in the same folder as the program and try again!')
            sleep(3)

    
    while True:
        typo = input(f"\n{ques} Enter the type of your proxies:\n[{c('1')}] HTTP/S\n[{c('2')}] SOCKS4\n[{c('3')}] SOCKS5\n >> ")
        if typo in '123':
            break
        else:
            print(exl+' Error! Enter only the following: 1, 2 or 3')
            sleep(2)
    
    
    for proxy in proxies_a:
        if typo == '1':
            proxies.append({
                'http':f'https://{proxy}',
                'https':f'http://{proxy}'
            })
        elif typo == '2':
            proxies.append({
                'http':f'socks4://{proxy}',
                'https':f'socks4://{proxy}'
            })
        elif typo == '3':
            proxies.append({
                'http':f'socks5://{proxy}',
                'https':f'socks5://{proxy}'
            })
else:
    proxies.append(dict())




if mode == '1':
    with open('vulnerable_sites.txt','w', encoding='utf-8') as fill:
        pass
    threads = input(ques+' How many threads u want? \n--------------> ')
    clear()
    print(logo)
    for _ in range(int(threads)):
        thread1 = threading.Thread(target=vulnerability)
        thread1.start()

elif mode == '2':
    with open('exist_sites.txt','w', encoding='utf-8') as fill:
        pass
    threads = input(ques+' How many threads u want? \n--------------> ')
    clear()
    print(logo)
    for _ in range(int(threads)):
        thread1 = threading.Thread(target=existence)
        thread1.start()


# Checks every second if the program is finished or not    
running = True
def CheckThreads():
    global running
    if threading.active_count() == 1:
        running = False

schedule.every().second.do(CheckThreads)

while running:
    schedule.run_pending()
    sleep(1)


# The program is stopped
if not running:
    print('\n'+ha+' Done checking!')
    if mode == '1':
        print(mult+f' All Vulnerable websites will be saved in {b("vulnerable_sites.txt")}')
    else:
        print(mult+f' All live websites will be saved in {b("exist_sites.txt")}')
    input('\n')

