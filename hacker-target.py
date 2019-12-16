import os
import requests
import platform
from halo import Halo
import validators
from art import *
from termcolor import colored

version = "version 1.0"
author = "Made by Rich\n"

def check_status():
    print(colored("[#] Checking the availability of API server...", "magenta"))
    request = requests.get("https://hackertarget.com")
    http = request.status_code
    if http == 200:
        print(colored("[#] API Server is ", "magenta") + colored("Online\n", "green"))
    else:
        print(colored("[!] Oops Error occured, Server offline\n", "red"))
        exit()

def whois(host):
    print("\n##### Whois Lookup #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/whois/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))

def traceroute(host):
    print("\n##### Traceroute #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/mtr/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))

def dnslookup(host):
    print("\n##### DNS Lookup #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/dnslookup/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))

def reversedns(host):
    print("\n##### Reverse DNS Lookup #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/reversedns/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))   

def geoip(host):
    print("\n##### GeoIP Lookup #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/geoip/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))   

def portscan(host):
    print("\n##### Port Scan #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/nmap/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))   

def pagelinks(host):
    print("\n##### Page Links #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/pagelinks/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))   

def httpheader(host):
    print("\n##### HTTP Header #####\n")
    spinner = Halo(text="Loading", spinner="dots")
    spinner.start()
    result = requests.get("https://api.hackertarget.com/httpheaders/?q=" + host).content.decode("UTF-8")
    spinner.stop()
    print(colored(result,"yellow"))   
      
def print_menu():      
    print(colored(20 * "-" + " MENU " + 20 * "-", "cyan"))
    print(colored("[1] Whois", "cyan"))
    print(colored("[2] Traceroute", "cyan"))
    print(colored("[3] DNS Lookup", "cyan"))
    print(colored("[4] Reverse DNS", "cyan"))
    print(colored("[5] GeoIP Lookup", "cyan"))
    print(colored("[6] Port Scan", "cyan"))
    print(colored("[7] Page Links", "cyan"))
    print(colored("[8] HTTP Header", "cyan"))
    print(colored("[9] Exit", "cyan"))
    print(colored(46 * "-", "cyan"))

def isIP(str):
    try:
        IP(str)
    except ValueError:
        return False
    return True

def main():
    loop = True
    while loop:
        # Check OS
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")

        # Print some badass ascii art header here !
        print("\n")
        tprint("HackerTarget",font="rnd-medium")
        print(colored(version, "green"))
        print(colored(author, "blue"))

        # Check server status
        check_status()

        # Displays menu and choose options
        print_menu()    
        choice = input("Enter your choice [1-9]: ")
        if choice == "1":
            host = input("Enter IP or Domain for lookup: ")
            if validators.domain(host) or validators.ipv4(host):
                whois(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "2":
            host = input("Enter IP or Domain for lookup: ")
            if validators.domain(host) or validators.ipv4(host):
                traceroute(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "3":
            host = input("Enter Domain for lookup: ")
            if validators.domain(host):
                dnslookup(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "4":
            host = input("Enter IP or Domain for lookup: ")
            if validators.domain(host) or validators.ipv4(host):
                reversedns(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "5": 
            host = input("Enter IP for lookup: ")
            if validators.ipv4(host):
                geoip(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "6":
            host = input("Enter IP or Domain for lookup: ")
            if validators.domain(host) or validators.ipv4(host):
                portscan(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "7":
            host = input("Enter Domain for lookup: ")
            if validators.domain(host):
                pagelinks(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "8":
            host = input("Enter Domain for lookup: ")
            if validators.domain(host):
                httpheader(host)
            else:
                print(colored("Something wrong with input!", "red"))
            input("Press [Enter] to continue...")
        elif choice == "9":
            print("Thank you for using!")
            loop=False
        else:
            print(colored("Wrong option selection. Enter any key to try again..", "red"))
        
if __name__ == "__main__":
    main()
