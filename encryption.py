from hashlib import*
import pyfiglet
from termcolor import colored
import os
os.system("cls")
encryption = pyfiglet.figlet_format("encryption")
print(colored(encryption,'blue'))
print(colored("                    alhasan alharbi",'red'))


print(r""" sha1 [1]  
 sha512 [2]  sha3_512 [3] 
 sha224 [4]  md5  [5]   sha256 [6]  
 sha3_224 [7]  sha3_256 [8]  sha512 [9]  sha384 [10]""")
sha512
q=input("enter the options --> ")
if q=='1':
    os.system("cls")
    a=sha224(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=='2':
    os.system("cls")
    a=sha512(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=='3':
    os.system("cls")
    a=sha3_512(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=='4':
    os.system("cls")
    a=sha224(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="5":
    os.system("cls")
    a=md5(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="6":
    os.system("cls")
    a=sha256(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="7":
    os.system("cls")
    a=sha3_224(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="8":
    os.system("cls")
    a=sha3_256(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="9":
    os.system("cls")
    a=sha512(input("enter the password \n").encode()).hexdigest()
    print(a)
if q=="10":
    os.system("cls")
    a=sha384(input("enter the password \n").encode()).hexdigest()
    print(a)