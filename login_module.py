# login_module.py

def login_system():
    users = {"admin": "1234"}  # demo credentials
    print("===== LOGIN SYSTEM =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users and users[username] == password:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials! Access Denied.\n")
        return False