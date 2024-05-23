import socket

def main_menu():
    print ("Search headlines\n")
    print ("List of scources\n")
    print ("Quit\n")
    option = input("Choose an option = \n")
    if (option == 1):
        print ("\n")
    elif (option == 2):
        print ("\n")
    elif (option == 3): 
        print ("\n")


def start_client():
    print("---------- Welcome to news API ----------\n")
    print("Conecting to server ..\n")
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(("127.0.0.1",5349))
    print("----------Server Connected Successfully ----------\n")
    user_name = input("Enter your username: \n")
    cs.send(user_name.encode("utf-8"))
    main_menu()

if __name__ == "__main__":
    start_client()
