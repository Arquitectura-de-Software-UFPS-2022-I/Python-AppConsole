from signaturelib import services
import getpass
import os.path
from os import path

user = None


def request_login():
    global user
    print("Welcome back!")
    username = input("Please enter your username: ")
    password = getpass.getpass(prompt="Please enter your password: ", stream=None) 
    user = services.get_user_login(username, password)


def register_user():
    global user
    print("Welcome to the registration page!")
    name = input("Please enter your name: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    email = input("Please enter your email: ")
    user = services.register_user(name, email, username, password)


print("Welcome to the Signature Program UFPS")


def show_options():
    print("##########################")
    print("#         MENU           #")
    print("##########################")
    print("1. Upload a signature")
    print("2. Upload pdf file")
    print("3. Request a signature")
    print("4. Sign a document")
    print("5. Generate pdf file")
    print("6. List all signature requests approved")
    print("7. List all signature requests pending")
    print("8. List all of my pending signature requests")
    print("9. Signature history")
    print("10. Logout")


def upload_signature():
    global user
    path_signature = input("Please enter the path of the signature : ")
    if path.exists(path_signature):
        ext = path_signature.split(".")[-1] .lower()
        if ext == "png" or ext == "jpg":
            image = open(path_signature, "rb")
            if services.validate_signature(path_signature):
                services.insert_signature(user.id, os.path.basename(path_signature), path_signature)
                print("Signature uploaded successfully!")
            else:
                print("Invalid signature")
        else:
            print("Invalid file extension")
    else:
        print("Invalid path")


def upload_pdf():
    global user
    path_pdf = input("Please enter the path of the pdf : ")
    if path.exists(path_pdf):
        ext = path_pdf.split(".")[-1] .lower()
        if ext == "pdf":
            pdf = open(path_pdf, "rb")
            subject = input("Please enter the subject : ")
            services.register_request_signature(user.id, os.path.basename(path_pdf), path_pdf, subject)
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
    while not stop_selection:
        for iserf in users:
            print("{} - {}".format(iserf.id, iserf.full_name))
        ans = input("Select a user to request a signature or enter '0' to stop : ")
        if ans == "0":
            stop_selection = True
        else:
            num_page = input("Please select the page for the signature : ")
            pos_x = input("Please select the x position for the signature : ")
            pos_y = input("Please select the y position for the signature : ")
            for user_sl in users:
                if user_sl.id == int(ans):
                    dict_users[int(ans)] = (int(num_page), int(pos_x), int(pos_y))
                    users_selected.append(user_sl)
        users = [userS for userS in users if userS.id != int(ans)]

    for user_selected in users_selected:
        services.register_request_signature_user(request.id, user_selected.id, dict_users[user_selected.id][1], dict_users[user_selected.id][2], dict_users[user_selected.id][0])
    print("Request sent successfully!")


def sign_document():
    if user.signature != None:
        my_request_signature = services.get_list_signature_request_user_by_user_id_and_signed(user.id, False)
        print("Please select a request to sign: ")
        signature_request = {}
        for request in my_request_signature:
            if not request.request in signature_request:
                signature_request[request.request] = services.get_signature_request(request.request)
            print("{} - {}".format(request.id,
                signature_request[request.request].subject))
        ans = input("Select a request to sign")
        services.approve_signature((int(ans)))
        print("Signature approved successfully!")
    else:
        print("You don't have a signature")


def generate_pdf():
    my_request_signature = services.get_request_signature_by_user(user.id)
    print("Please select a request to sign: ")
    for request in my_request_signature:
        print("{} - {}".format(request.id, request.subject))
    ans = input("Select a request to sign")
    dir = input("Insert the path of the directory where you want to save the pdf file")
    if path.exists(dir) and path.isdir(dir):
        document_bytes = services.get_file_pdf(int(ans))
        with open(dir+"/document.pdf", "wb") as f:
            f.write(document_bytes)
        print("PDF file generated successfully!")


def list_all_signature_requests(approved: bool):
    my_request_signature = services.get_request_signature_by_user(user.id)
    print("My signature requests {} : ".format("approved" if approved else "pending"))
    for my_request_signature in my_request_signature:
        print("{} - {}".format(my_request_signature.id, my_request_signature.subject))
    request_id = input("Select a request to  show the signatures approved :")

    list_signature_requests_approved = services.get_list_signature_request_user_by_request_id_and_signed(request_id, approved)
    print("Signatures {}: for the request {}".format("approved" if approved else "pending", request_id))
    signature_request = {}
    users = {}
    for request in list_signature_requests_approved:
        if not request.request in signature_request:
            signature_request[request.request] = services.get_signature_request(request.request)
        if not request.user in users:
            users[request.user] = services.get_user(request.user)
        print("{} - {} - {}".format(request.id, signature_request[request.request].subject, users[request.user].full_name))


def list_all_my_pending_signature_requests():
    my_request_signature = services.get_list_signature_request_user_by_user_id_and_signed(user.id, False)
    print("My pending signature requests: ")
    signature_request = {}
    for request in my_request_signature:
        if not request.request in signature_request:
            signature_request[request.request] = services.get_signature_request(request.request)
        print("{} - {}".format(request.id, signature_request[request.request].subject))


def list_all_signature_history():
    my_request_signature = services.get_list_signature_request_user_by_user_id_and_signed(user.id, True)
    print("My signature history: ")
    signature_request = {}
    for request in my_request_signature:
        if not request.request in signature_request:
            signature_request[request.request] = services.get_signature_request(request.request)
        print("{} - {} - {}".format(request.id, signature_request[request.request].subject, request.signature_date))


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
    elif ans == "4":
        sign_document()
    elif ans == "5":
        generate_pdf()
    elif ans == "6":
        list_all_signature_requests(True)
    elif ans == "7":
        list_all_signature_requests(False)
    elif ans == "8":
        list_all_my_pending_signature_requests()
    elif ans == "9":
        list_all_signature_history()
    elif ans == "10":
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
        while user == None:
            request_login()

    else:
        print("Invalid option")
        exit()

    if user != None:
        main()


if __name__ == "__main__":
    start_system()
