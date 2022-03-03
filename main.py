from pkgutil import extend_path
from tkinter import EW
from signaturelib import services
import os.path
from os import path

user = None

def request_login():
    global user
    print("Welcome back!")
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    user = services.get_user_login(username, password)


def register_user():
    global user
    print("Welcome to the registration page!")
    name = input("Please enter your name:")
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    email = input("Please enter your email:")
    user = services.register_user(name,email, username, password)


print("Welcome to the Signature Program UFPS")

def start_system():
    
    ans = input("Do you have a account? (Y/N)").lower()

    if ans == "y":

        while user == None:
            request_login()
            
    elif ans == "n":
        register_user()

    else :
        print("Invalid option")
        exit()   
    


if __name__ == "__main__":
    start_system()