from optparse import OptionParser
from urllib3 import request
import json
import requests
from functools import wraps
from blockchain import *
import sys
import re
import time
import codecs
import os
from termcolor import colored
import glob
global worknow
global trynow

## Important this code will not run on python 2.7, you must use python 3.5 or 3.6

##  sudo apt-get install python-setuptools python-dev build-essential.
## python3.4 -m pip install SomePackage
## sudo python3.4 -m pip install blockchain
##  sudo python3.4 -m pip install termcolor
## pip install blockchain
## sudo python3.5 -m pip install urllib3


# install  pip libraries with python3.6 python3.6 -m pip install --upgrade pip
# sudo python3.6 -m pip install termcolor
#you also must install the blockchain modules as well.


def lookup_id_single(symbol):
    global temp7
    global worknow
    master = []

    t1 = []
    t2 = []
    # sample b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da
    try:
        url5 = "https://blockchain.info/rawtx/"
        symbol = str(symbol)
        url5 = url5 + symbol
        # print(url2)
        r = requests.get(url5)
        if r.status_code == 200:

            # The next three if statements are necessary to weed out unusal Transaction IDs,
            # such as transactions with newly generatated which do not list  wallet addr on input
            if 'prev_out' in r.json()['inputs'][0]:
                if len(r.json()['inputs'][0]['prev_out']) >= 1:
                    temp = r.json()['inputs']
                    if temp[0]['prev_out']:
                        count2 = 0
                        for i in range(0, len(r.json()['inputs'])):
                            # global temp7
                            # global appendFile

                            temp7 = str(tempt) + '_results'
                            print(temp7)
                            print(temp7)
                            print(temp7)
                            print('checking output filename', temp7)
                            worknow = open(temp7, 'w')

                            print(
                                        "Start Transaction ========================== [" + symbol + "] ============================ Start Transaction\n")
                            worknow.write(
                                "Start Transaction ========================== [" + symbol + "] ============================ Start Transaction\n")
                            worknow.write('\n')
                            print(colored("Wallets by Input Addr involved in the Transaction. \n", 'blue'))
                            worknow.write("Wallets by Input Addr involved in the Transaction. \n")
                            worknow.write('\n')
                            try:
                                ins_adds = r.json()['inputs'][i]['prev_out']['addr']
                                ins_vals = r.json()['inputs'][i]['prev_out']['value']
                                ins_vals2 = round((float(r.json()['inputs'][i]['prev_out']['value']) / 100000000), 12)
                                itemsx = [ins_adds, ins_vals, ins_vals2]
                                itemsx = list(itemsx)
                                if len(itemsx) >= 1:
                                    print(colored("Input addr_wallet" + str(
                                        count2) + ":  " + ins_adds + "   value of transaction: " + str(
                                        ins_vals) + "   value in BTC:  " + str(ins_vals2), 'green'))
                                    count2 += 1
                                    worknow.write("Input addr_wallet" + str(
                                        count2) + ":  " + ins_adds + "   value of transaction: " + str(
                                        ins_vals) + "   value in BTC:  " + str(ins_vals2))
                                    worknow.write('\n')
                                    t1.append(itemsx)
                                else:
                                    break
                            except ValueError:
                                pass
                        print(
                            "------------------------------ Break, output wallets ----------------------------------------------\n")
                        worknow.write(
                            "------------------------------ Break, output wallets ----------------------------------------------\n")
                        worknow.write('\n')

        if len(r.json()['out']) >= 1:
            count3 = 0
            temp2 = r.json()['out']
            for i in range(0, len(r.json()['out'])):
                temp10 = temp2[i]
                if len(temp10) >= 7:
                    try:
                        outs_adds = r.json()['out'][i]['addr']
                        outs_vals = r.json()['out'][i]['value']
                        outs_vals2 = round((float(r.json()['out'][i]['value']) / 100000000), 12)
                        items5 = [str(outs_adds), str(outs_vals), str(outs_vals2)]
                        items5 = list(items5)
                        print(colored(
                            "Rec_addr_wallet" + str(count3) + ": " + outs_adds + "   value of transaction: " + str(
                                outs_vals) + "   value in BTC:  " + str(outs_vals2) + '\n', 'red'))
                        count3 += 1
                        worknow.write(
                            "Rec_addr_wallet" + str(count3) + ": " + outs_adds + "   value of transaction: " + str(
                                outs_vals) + "   value in BTC:  " + str(outs_vals2) + '\n')
                        worknow.write('\n')
                        if len(items5) >= 1:
                            t2.append(items5)
                        else:
                            break
                    except ValueError:
                        pass
                else:
                    continue

            print(
                        "End Transaction ==================================== " + symbol + "   ========================= End Transaction\n\n\n")
            worknow.write(
                "End Transaction ==================================== " + symbol + "   ========================= End Transaction\n\n\n")
            worknow.write('\n')
            # master.append(t2)
            tmp = [t1, t2]
            worknow.close()

            return tmp



        else:
            pass

    except ValueError:
        pass

def lookup_id_bulk(symbol):
    global temp7
    global worknow    
    master = []

    t1 = []
    t2 = []
    # sample b6f6991d03df0e2e04dafffcd6bc418aac66049e2cd74b80f14ac86db1e3f0da
    try:
        url5 ="https://blockchain.info/rawtx/"
        symbol = str(symbol)
        url5 = url5 + symbol
        #print(url2)
        r = requests.get(url5)
        if r.status_code == 200:

            # The next three if statements are necessary to weed out unusal Transaction IDs,
            # such as transactions with newly generatated which do not list  wallet addr on input
            if 'prev_out' in r.json()['inputs'][0]:
                if len(r.json()['inputs'][0]['prev_out']) >= 1:
                    temp = r.json()['inputs']
                    if temp[0]['prev_out']:
                        count2 = 0
                        for i in range(0, len(r.json()['inputs'])):
                            #global temp7
                            #global appendFile
                            
                            
                            temp7 = str(tempT) + '_results' 
                            print(temp7)
                            print(temp7)
                            print(temp7)
                            print('checking output filename',temp7)
                            worknow = open(temp7, 'w')
                                
                                
                            
                            
                            print("Start Transaction ========================== [" + symbol + "] ============================ Start Transaction\n")
                            worknow.write("Start Transaction ========================== [" + symbol + "] ============================ Start Transaction\n")
                            worknow.write('\n')
                            print(colored("Wallets by Input Addr involved in the Transaction. \n", 'blue'))
                            worknow.write("Wallets by Input Addr involved in the Transaction. \n")
                            worknow.write('\n')
                            try:
                                ins_adds = r.json()['inputs'][i]['prev_out']['addr']
                                ins_vals = r.json()['inputs'][i]['prev_out']['value']
                                ins_vals2 = round((float(r.json()['inputs'][i]['prev_out']['value'])/100000000), 12)
                                itemsx = [ins_adds, ins_vals, ins_vals2]
                                itemsx = list(itemsx)
                                if len(itemsx) >=1:
                                    print(colored("Input addr_wallet"+ str(count2) + ":  " + ins_adds + "   value of transaction: " + str(ins_vals) + "   value in BTC:  " + str(ins_vals2), 'green'))
                                    count2 += 1
                                    worknow.write("Input addr_wallet"+ str(count2) + ":  " + ins_adds + "   value of transaction: " + str(ins_vals) + "   value in BTC:  " + str(ins_vals2))
                                    worknow.write('\n')
                                    t1.append(itemsx)
                                else:
                                    break
                            except ValueError:
                                pass
                        print("------------------------------ Break, output wallets ----------------------------------------------\n")
                        worknow.write("------------------------------ Break, output wallets ----------------------------------------------\n")
                        worknow.write('\n')
    




        if len(r.json()['out']) >= 1:
            count3 = 0
            temp2 = r.json()['out']
            for i in range(0, len(r.json()['out'])):
                temp10 = temp2[i]
                if len(temp10) >= 7:
                    try:
                        outs_adds = r.json()['out'][i]['addr']
                        outs_vals = r.json()['out'][i]['value']
                        outs_vals2 = round((float(r.json()['out'][i]['value'])/100000000), 12)
                        items5 = [str(outs_adds), str(outs_vals), str(outs_vals2)]
                        items5 = list(items5)
                        print(colored("Rec_addr_wallet"+ str(count3) +": " + outs_adds + "   value of transaction: " + str(outs_vals) + "   value in BTC:  " + str(outs_vals2) +'\n', 'red'))
                        count3 += 1
                        worknow.write("Rec_addr_wallet"+ str(count3) +": " + outs_adds + "   value of transaction: " + str(outs_vals) + "   value in BTC:  " + str(outs_vals2) +'\n')
                        worknow.write('\n')
                        if len(items5) >= 1:
                            t2.append(items5)
                        else:
                            break
                    except ValueError:
                        pass
                else:
                    continue

            print("End Transaction ==================================== " + symbol + "   ========================= End Transaction\n\n\n")
            worknow.write("End Transaction ==================================== " + symbol + "   ========================= End Transaction\n\n\n")
            worknow.write('\n')
            # master.append(t2)
            tmp = [t1, t2]
            worknow.close()

            return tmp
            

        
        else:
            pass

    except ValueError:
        pass


def lookup_file_single(symbol):
    """Look up quote for symbol."""

    # reject symbol if does not start with 1 or 3
    # if symbol.startswith("1") or symbol.startswith("3"):

    if ((len(symbol) >= 26 and len(symbol) <= 34) and ((symbol.startswith("1") or symbol.startswith("3")))):
        # if (len(symbol) >= 26 and len(symbol) <= 34):
        # If the wallet is not of the correct length or only hex characters reject
        for i in symbol:
            if i.isdigit() or i.isalpha():
                if i != 'l' and i != 'I' and i != 'O' and i != '0':
                    pass
                else:
                    failed.append(symbol)

        try:
            url2 = "https://blockchain.info/rawaddr/"
            symbol = str(symbol) + '?limit=1'
            url2 = url2 + symbol
            # print(url2)
            our_data = requests.get(url2).json()

            add2 = our_data['address']
            trans = our_data['n_tx']
            # All bitcoin values are in Satoshi i.e. divide by 100000000 to get the amount in BTC
            rec = our_data['total_received'] / 100000000
            sent = our_data['total_sent'] / 100000000
            bal = our_data['final_balance'] / 100000000
            # bal = bal/100000000
            data = [add2, trans, rec, sent, bal]
            results = []
            results.append(data)
            header = ['Wallet Addr', 'Number Transactions', 'Amount Received', 'Amount Sent', 'Wallet Balance']
            output = {}
            x = 0
            global trynow
            global temp77
            global test_test
            global tempW
            global tempw
            # test_test = tempW
            temp77 = str(tempw) + '_results'
            if os.path.exists(temp77):
                permission = 'a'

            else:
                permission = 'w'

            print(temp77)
            print('checking output filename', temp77)
            trynow = open(temp77, permission)
            for lists in results:
                print(colored('Wallet Addr:  ' + lists[0] + '  Number Transactions:  ' + str(
                    lists[1]) + "    Amount Received:  " + str(lists[2]) + '   Amount Sent:  ' + str(
                    lists[3]) + '  Wallet Balance:  ' + str(lists[4]), 'red'))
                trynow.write('\n')
                trynow.write('Wallet Addr:  ' + lists[0] + '  Number Transactions:  ' + str(
                    lists[1]) + "    Amount Received:  " + str(lists[2]) + '   Amount Sent:  ' + str(
                    lists[3]) + '  Wallet Balance:  ' + str(lists[4]))
                # Please limit your queries to a maximum of 1 every 10 seconds.
                time.sleep(1)
            return trynow

        except ValueError:
            pass

    else:
        return None






def lookup_file_bulk(symbol):
    """Look up quote for symbol."""

    # reject symbol if does not start with 1 or 3
    # if symbol.startswith("1") or symbol.startswith("3"):

    if ((len(symbol) >= 26 and len(symbol) <= 34) and ((symbol.startswith("1") or symbol.startswith("3")))):
        # if (len(symbol) >= 26 and len(symbol) <= 34):
            # If the wallet is not of the correct length or only hex characters reject
            for i in symbol:
                if i.isdigit() or i.isalpha():
                    if i != 'l' and i != 'I' and i != 'O' and i != '0':
                        pass
                    else:
                        failed.append(symbol)

            try:
                url2 ="https://blockchain.info/rawaddr/"
                symbol = str(symbol) + '?limit=1'
                url2 = url2 + symbol
                #print(url2)
                our_data = requests.get(url2).json()

                add2 = our_data['address']
                trans = our_data['n_tx']
                # All bitcoin values are in Satoshi i.e. divide by 100000000 to get the amount in BTC
                rec = our_data['total_received']/100000000
                sent = our_data['total_sent']/100000000
                bal = our_data['final_balance']/100000000
                # bal = bal/100000000
                data = [add2, trans, rec, sent, bal]
                results = []
                results.append(data)
                header = ['Wallet Addr', 'Number Transactions', 'Amount Received', 'Amount Sent', 'Wallet Balance']
                output = {}
                x = 0
                global trynow
                global temp77
                global test_test
                global tempW
                global tempw
                global permission

                # test_test = tempW
                temp77 = str(tempW) + '_results'
                if os.path.exists(temp77):
                    permission = 'a'
                    
                else:
                    permission = 'w'

                global tempWout
                    
                print(temp77)
                print('checking output filename',temp77)

                with open(temp77, permission, encoding="ascii", errors="surrogateescape") as tempWout:
                    for lists in results:
                        print(colored('Wallet Addr:  ' + lists[0] + '  Number Transactions:  ' + str(lists[1]) + "    Amount Received:  " + str(lists[2]) + '   Amount Sent:  ' + str(lists[3]) + '  Wallet Balance:  ' + str(lists[4]), 'red'))
                        tempWout.write('\n')
                        tempWout.write('Wallet Addr:  ' + lists[0] + '  Number Transactions:  ' + str(lists[1]) + "    Amount Received:  " + str(lists[2]) + '   Amount Sent:  ' + str(lists[3]) + '  Wallet Balance:  ' + str(lists[4]))
                        # Please limit your queries to a maximum of 1 every 10 seconds.
                        time.sleep(1)
                        return tempWout

            except ValueError:
                pass

    else:
        return None




def removehtml(text):
    step1 = re.compile('<.*?>')
    clean = re.sub(step1, '', text)
    return clean

usage = '''usage: %prog -t file.txt , will scrape BTC transaction ID from text file, -w scrape BTC Wallets Address from text file
           if you wish to do bulk analysis on many files in a set directory, you must add the -W switch for bulk scrape files for BTC wallets and -T to bulk scrape,
           for transaction ID .. usage: %prog -W or %prog -T'''
parser = OptionParser(usage)
parser.add_option("-w", action="store", type="string", dest='w', help = "Follow -w with the name of text file you want to scrape for BTC Wallet Addresses")
parser.add_option("-t", action="store", type="string", dest='t', help = "Follow -t with text file you wish to check for BTC transaction ids")
parser.add_option("-W", action="store", type="string", dest='W', help = "The -W option will scrape recursively through a directory for BTC wallets address for example  usage: %prog -W /home/xxx/Downloads/shaddy/btc-test/  ")
parser.add_option("-T", action="store", type="string", dest='T', help = "The -T will scrape recursively through a directory for BTC transaction IDs") 
(options,args) = parser.parse_args()



failed = []
bad_id = []

if options.T:
    x = sys.argv[2]
    ## input("list path to directory where you files are located, for example /home/xxx/Downloads/shaddy/btc-test/  !: ")

    os.path.isdir(x)

    if os.path.isdir(x):
        print('Reading from directory', x)
        tmp = []
        y = glob.glob(x+'**/*', recursive=True)
    
        for files in y:
            
            failed = []
            print('Reading from file:  ', files)
            global tempT
            tempT = files
            
            with open(files, 'r', encoding="ascii", errors="surrogateescape") as f:
                try:
                    data_st = f.read().rstrip()
                    # data_st = removehtml(data_st)
                    # print(len(data_st))
                    print('file data has been read, the API key allows 1 query every 10 seconds so be patient... grab some coffee.\n')
                    f1 = re.split(' |, |\"|\n|:|\: |:  |\.|\<|\>|\+|-|=|_|\'|{|}|\[|\]|@|/|,|\r|. ', data_st)
        
                    n = set(f1)
                    end = list(n)
        
                    count = 0
                    # print('Reading from file:  ', sys.argv[2])
                    ids = []
                    for x in end:
                        if (len(x) == 64):
        
                            for i in x:
        
                                if ((i >= 'a' and i <= 'f') or (i >= 'A' and i <= 'F') or (i.isdigit())):
                                    count += 1
        
                                else:
                                    break
                            ids.append(x)
        
                        else:
                            continue
                    l1 = []
                    for wallets in ids:
                        l1.append(lookup_id_bulk(wallets))
                        
                    #worknow = worknow
        
                    l1 = list(filter(None.__ne__,l1))
        
                    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        
                    price = r.json()['bpi']['USD']['rate']
                    print('The current price of BTC is: ' + price+'\n')
                    #appendFile.write('\n')  
                    #worknow.close()
                    f.close()
        
        
                except UnicodeEncodeError:
                    pass                

elif options.W:
    x = sys.argv[2]
    ## input("list path to directory where you files are located, for example /home/xxx/Downloads/shaddy/btc-test/  !: ")

    os.path.isdir(x)

    if os.path.isdir(x):
        print('Reading from directory', x)
        tmp = []
        y = glob.glob(x+'**/*', recursive=True)
    
        for files in y:
            # global tempW
            failed = []
            print('Reading from file:  ', files)

            tempW = str(files)
            with open(files, 'r', encoding="ascii", errors="surrogateescape") as f:
                try:

                    data_st = f.read().strip()
                    data_st = removehtml(data_st)
                    #data_st = data_st.rstrip('\r\n')
                    #data_st = data_st.split()
                    
                    print('file data has been read, the API key allows 1 query every 10 seconds so be patient... grab some coffee.\n')
                    f1 = re.split(' |, |\"|\n|:|\: |:  |\.|\<|\>|\+|-|=|_|\'|r"\'"|{|}|\[|\]|@|/|,|\r|. ', data_st)
                    n = set(f1)
                    end = list(n)
        
                    count = 0
        
                    for x in end:
                        lookup_file_bulk(x)

                        count += 1
                        if count % 10000 == 0:
                            print(count)
        
                    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        
                    price = r.json()['bpi']['USD']['rate']
                    with open(tempWout, 'a', encoding="ascii", errors="surrogateescape") as t2W:
                        print('The current price of BTC is: ' + price + '\n')
                        t2W.write('The current price of BTC is: ' + price)
                    
        
        
                        count = len(failed)
                        print('The program finished with', str(count) + ' false positives ')
                        t2W.write('\n')
                    f.close()
                    t2W.close()
                    #.close()
                    

                                      
        
                except UnicodeEncodeError:
                    
                    pass
                    
                
        
        #trynow.close()  
        #files.close()
    else:
        print("There may have been a typo, directory does not exist", x)



elif options.t:
    ## with open(sys.argv[2], 'r') as f:
    files = sys.argv[2]
    with open(files, 'r', encoding="ascii", errors="surrogateescape") as f:
        tempt = files
        try:
            data_st = f.read().rstrip()
            # data_st = removehtml(data_st)
            # print(len(data_st))
            print('file data has been read, the API key allows 1 query every 10 seconds so be patient... grab some coffee.\n')
            f1 = re.split(' |, |\"|\n|:|\: |:  |\.|\<|\>|\+|-|=|_|\'|{|}|\[|\]|@|/|,|\r|. ', data_st)

            n = set(f1)
            end = list(n)

            count = 0
            print('Reading from file:  ', sys.argv[2])
            ids = []
            for x in end:
                if (len(x) == 64):

                    for i in x:

                        if ((i >= 'a' and i <= 'f') or (i >= 'A' and i <= 'F') or (i.isdigit())):
                            count += 1

                        else:
                            break
                    ids.append(x)

                else:
                    continue
            l1 = []
            for wallets in ids:
                l1.append(lookup_id_single(wallets))

            l1 = list(filter(None.__ne__,l1))

            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

            price = r.json()['bpi']['USD']['rate']
            print('The current price of BTC is: ' + price+'\n')


        except UnicodeEncodeError:
            pass


elif options.w:
    failed = []
    print('Reading from file:  ', sys.argv[2])
    files = sys.argv[2]
    tempw = files
    with open(sys.argv[2], 'r', encoding="ascii", errors="surrogateescape") as f:
        try:
            data_st = f.read().strip()
            data_st = removehtml(data_st)
            print('file data has been read, the API key allows 1 query every 10 seconds so be patient... grab some coffee.\n')
            f1 = re.split(' |, |\"|\n|:|\: |:  |\.|\<|\>|\+|-|=|_|\'|r"\'"|{|}|\[|\]|@|/|,|\r|. ', data_st)
            n = set(f1)
            end = list(n)

            count = 0

            for x in end:
                lookup_file_single(x)
                count += 1
                if count % 10000 == 0:
                    print(count)

            r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

            price = r.json()['bpi']['USD']['rate']



            print('The current price of BTC is: ' + price + '\n')


            count = len(failed)
            print('The program finished with', str(count) + ' false positives ')

        except UnicodeEncodeError:
            pass

else:
    print(usage)
    
    



