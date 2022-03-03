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


def show_options():
    print("1. Upload a signature")
    print("2. Upload pdf file")
    print("3. Request a signature")
    print("4. Sign a document")
    print("5. Generate pdf file")
    print("6. List all signature requests approved")
    print("7. List all signature requests pending")
    print("8. List all of my pending signature requests")
    print("9. Signature history")
    print("0. Logout")


def upload_signature():
    global user
    path_signature = input("Please enter the path of the signature : ")
    if path.exists(path_signature):
        ext = path_signature.split(".")[-1] .lower()
        if ext == "png" or ext == "jpg":
            image = open(path_signature, "rb")
            if services.validate_signature(path_signature):
                services.insert_signature(user.id,image.name,image.read())
                print("Signature uploaded successfully!")
            else :
                print("Invalid signature")
        else:
            print("Invalid file extension")
    else:
        print("Invalid path")


def main():
    global user
    show_options()
    ans = input("Please enter your option: ")
    if ans == "1":
        upload_signature()
    elif ans == "0":
        print("Logging out...")
        user = None
    else:
        print("Invalid option")
        exit()
    if user != None:
        main()
        

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

    if user != None:
        main()


if __name__ == "__main__":
    start_system()