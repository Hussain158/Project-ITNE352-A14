import socket

def send(option,cs):
    cs.send(option.encode("utf-8"))
    
def main_menu(cs):
    print ("1.Search headlines\n")
    print ("2.List of scources\n")
    print ("3.Quit\n")
    option = input("Choose an option = \n")
    if (option == 1):
        headline_search(cs)
    elif (option == 2):
        list_of_sources(cs)
    elif (option == 3):
        cs.close()

def headline_search(cs):
    print("1.Search for keywords\n")
    print("2.Search by category\n")
    print("3.Search by country\n")
    print("4.List all new headlines\n")
    print("5.Back to main menu\n")
    option = input("Choose an option = \n")
    if option in (1,2,3,4):
        send(option,cs)
    elif option == 5:
        main_menu(cs)
        
def list_of_sources(cs):
    print("1.Search by category\n")
    print("2.Search by country\n")
    print("3.Search by language\n")
    print("4.List all\n")
    print("5.Back to the main menu\n")
    option = input("Choose an option = \n")
    if option in (1,2,3,4):
        send(option,cs)
    elif option == 5:
        main_menu(cs)
    
def start_client():
    print("---------- Welcome to news API ----------\n")
    print("Conecting to server ..\n")
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(("127.0.0.1",5349))
    print("----------Server Connected Successfully ----------\n")
    user_name = input("Enter your username: \n")
    cs.send(user_name.encode("utf-8"))
    main_menu(cs)

if __name__ == "__main__":
    start_client()
