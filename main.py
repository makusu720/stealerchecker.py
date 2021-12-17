import sys
import os
import time
import regex as re
from colorama import Fore, Style
import shutil


def dump_pass():
    urls_regex = r"\bURL:\s+\K\S+"
    username_regex = r"\bUsername:\s+\K\S+"
    password_regex = r"\bPassword:\s+\K\S+"

    url_array = []
    username_array = []
    password_array = []
    file_path_array = []

    for i in items:
        i = path + "/" + i + "/Passwords.txt"

        try:
            file = open(i)
            file_string = file.read()
            file.close()
        except FileNotFoundError:
            continue

        urls = re.findall(urls_regex, file_string)
        usernames = re.findall(username_regex, file_string)
        passwords = re.findall(password_regex, file_string)

        if len(urls) == len(usernames) and len(usernames) == len(passwords):
            a = 0
            while a < len(urls):
                url_array.append(urls[a])
                username_array.append(usernames[a])
                password_array.append(passwords[a])
                file_path_array.append(i)
                a += 1
        else:
            print("Something went wrong")
    return url_array, username_array, password_array, file_path_array


def getcc():
    holder_regex = r"\bHolder:\s+\K\S+\s+\S+"
    cardtype_regex = r"\bCardType:\s+\K\S+"
    card_regex = r"\bCard:\s+\K\S+"
    expire_regex = r"\bExpire:\s+\K\S+"

    for i in items:
        i = path + "/" + i + "/CreditCards"
        try:
            cc = os.listdir(i)
        except FileNotFoundError:
            continue

        for n in cc:
            n = i + "/" + n
            file = open(n)
            file_string = file.read()
            file.close()
            holders = re.findall(holder_regex, file_string)
            cardtypes = re.findall(cardtype_regex, file_string)
            card = re.findall(card_regex, file_string)
            expire = re.findall(expire_regex, file_string)

            if len(holders) == len(cardtypes) and len(cardtypes) == len(card) and len(card) == len(expire):
                print(f"{Fore.GREEN}{n} - {len(holders)} cards!{Style.RESET_ALL}")
                a = 0
                while a < len(holders):
                    print(holders[a].replace("CardType: Unknown", "UNKNOWN"))
                    print(cardtypes[a])
                    print(card[a])
                    print(expire[a])
                    print("============================")

                    if verbose:
                        file = open(r"./.temp/" + i + "/Password.txt", "a")
                        file.write(f"{holders[a].replace('CardType: Unknown', 'UNKNOWN')}\n{cardtypes[a]}\n{card[a]}\n{expire[a]}\n============================\n")

                    a += 1
            else:
                print("Something went wrong")


def getdc():
    pass


def getexodus():
    for i in items:
        i1 = path + "/" + i + "/Wallets/Exodus/"
        try:
            os.listdir(i1)
        except FileNotFoundError:
            continue

        shutil.copytree(i1, r"./.temp/" + i + "/")


def getwalletmenu():
    print("1. Exodus\n2. Coming Soon")

    try:
        selected_menu = int(input("Select: "))

        if selected_menu == 1:
            getexodus()
        elif selected_menu == 2:
            pass
        else:
            print("Please write a valid number")
            time.sleep(100)
            os.system('clear')
            getwalletmenu()
    except ValueError:
        pass


def getmenu():
    print(f"Loaded: {Fore.YELLOW}{len(items)}{Style.RESET_ALL} logs\n")
    print("1. CC's\n2. FTP's\n3. Discord\n4. Telegram\n5. Wallet's")

    try:
        selected_menu = int(input("Select: "))

        if selected_menu == 1:
            getcc()
        elif selected_menu == 2:
            pass
        elif selected_menu == 3:
            getdc()
        elif selected_menu == 4:
            pass
        elif selected_menu == 5:
            getwalletmenu()
        else:
            print("Please write a valid number")
            time.sleep(100)
            os.system('clear')
            startmenu()

    except ValueError:
        print("Please write a number")
        time.sleep(100)
        os.system('clear')
        getmenu()


def search_url(search):
    dump = dump_pass()
    for i, e in enumerate(dump[0]):
        if search in e:
            print(f"{Fore.GREEN}{dump[3][i]}{Style.RESET_ALL}")
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")
            print(dump[1][i])
            print(dump[2][i])
            print("======================")


# TODO: Change to static input, currently same as search URL
def search_website(search):
    dump = dump_pass()
    for i, e in enumerate(dump[0]):
        if search in e:
            print(f"{Fore.GREEN}{dump[3][i]}{Style.RESET_ALL}")
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")
            print(dump[1][i])
            print(dump[2][i])
            print("======================")


def search_username(search):
    dump = dump_pass()
    for i, e in enumerate(dump[1]):
        if search in e:
            print(f"{Fore.GREEN}{dump[3][i]}{Style.RESET_ALL}")
            print(dump[0][1])
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")
            print(dump[2][i])
            print("======================")


def searchmenu():
    print(f"Loaded: {Fore.YELLOW}{len(items)}{Style.RESET_ALL} logs\n")
    print("1. Websites\n2. URL's\n3. Username\n4. Pass")

    try:
        selected_menu = int(input("Select: "))

        if selected_menu == 1:
            search_website("onlyfans.com")
        elif selected_menu == 2:
            search = input("URL to search: ")
            search_url(search)
        elif selected_menu == 3:
            search = input("Username/Email to search: ")
            search_username(search)
        elif selected_menu == 4:
            pass
        else:
            print("Please write a valid number")
            time.sleep(100)
            os.system('clear')
            startmenu()

    except ValueError:
        print("Please write a number")
        time.sleep(100)
        os.system('clear')
        getmenu()


# Load Start Menu
def startmenu():
    print(f"Loaded: {Fore.YELLOW}{len(items)}{Style.RESET_ALL} logs\n")
    print("1. Get\n2. Search\n3. Sort Logs\n4. Analysis")

    try:
        selected_menu = int(input("Select: "))

        if selected_menu == 1:
            getmenu()
        elif selected_menu == 2:
            searchmenu()
        elif selected_menu == 3:
            pass
        elif selected_menu == 4:
            pass
        else:
            print("Please write a valid number")
            time.sleep(100)
            os.system('clear')
            startmenu()

    except ValueError:
        print("Please write a number")
        time.sleep(100)
        os.system('clear')
        startmenu()


if sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print(sys.argv)
    print("This is the help page.")
elif sys.argv[1] == "-p" or sys.argv[1] == "--path":
    if sys.argv[3] == "-v" or sys.argv[3] == "--verbose":
        verbose = True
    else:
        verbose = False
    path = sys.argv[2]
    items = os.listdir(path)
    startmenu()
