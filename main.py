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
        ext = path_signature.split(".")[-1].lower()
        if ext == "png" or ext == "jpg":
            image = open(path_signature, "rb")
            if services.validate_signature(path_signature):
                services.insert_signature(user.id, os.path.basename(path_signature),image.read())
                print("Signature uploaded successfully!")
            else :
                print("Invalid signature")
        else:
            print("Invalid file extension")
    else:
        print("Invalid path")



def upload_pdf():
    global user
    path_pdf = input("Please enter the path of the pdf : ")
    if path.exists(path_pdf):
        ext = path_pdf.split(".")[-1].lower()
        if ext == "pdf" :
            pdf = open(path_pdf, "rb")
            subject = input("Please enter the subject : ")
            services.register_request_signature(user.id, os.path.basename(path_pdf),pdf.read(),subject)
            print("Request sent successfully!")

        else:
            print("Invalid file extension")
    else:
        print("Invalid path")


def request_signature():
    global user
    list_request_of_user = services.get_request_signature_by_user(user.id)
    for request in list_request_of_user:
        print("{} - {}".format(request.id, request.subject))
    request_id = input("Select a request to request a signature : ")
    users = services.list_users()
    users_selected = []
    stop_selection = False
    dict_users = {}
    while not stop_selection :
        
        for iserf in users:
            print("{} - {}".format(iserf.id, iserf.name))
           
        ans = input("Select a user to request a signature or enter '0' to stop : ")
       
        
        if ans == "0":
            stop_selection = True
        else:
            num_page = input("Please select the page for the signature : ")
            pos_x = input("Please select the x position for the signature : ")
            pos_y = input("Please select the y position for the signature : ")
            for user_sl in users :
                if user_sl.id == int(ans):
                    dict_users[int(ans)] = (int(num_page), int(pos_x), int(pos_y))
                    users_selected.append(user_sl)

        users = [userS for userS in users if userS.id != int(ans)]
    
    for user_selected in users_selected:
        services.register_request_signature_user(request.id, user_selected.id, dict_users[user_selected.id][1], dict_users[user_selected.id][2], dict_users[user_selected.id][0])
    print("Request sent successfully!")
    


def main():
    global user
    show_options()
    ans = input("Please enter your option: ")
    if ans == "1":
        upload_signature()
    elif ans == "2":
        upload_pdf()
    elif ans == "3":
        request_signature()
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