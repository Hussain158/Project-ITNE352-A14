import socket
import json
def main_menu():
    server_ip = "127.0.0.1"
    server_port = 4926
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")
    username = input("Enter your username: ")
    send_client(username, cs)
    while True:
        print("###################################################\n")
        print(f" welcome {username} please choose the desired option:  \n")
        print("1- search for a specific headlines")
        print("----------------------------------------------------")
        print("2- search for a specific list of sources")
        print("----------------------------------------------------")
        print("3- Quit the program")
        print("----------------------------------------------------")
        option = int(input("Enter your option: "))
        print("###################################################\n")
        if option == 1:
            headline_menu(cs)
        elif option == 2:
            sources_menu(cs)
        elif option == 3:
            print("goodbye, you are Quitting the program...")
            cs.close()
            break
        else:
            print("Invalid option. Please chooce and option from the list above")
def headline_menu(cs):
    #printing headline options and asking user to pick one.
    print("1- Search for Keywords")
    print("----------------------------------------------------")
    print("2- Search by Category")
    print("----------------------------------------------------")
    print("3- Search by Country")
    print("----------------------------------------------------")
    print("4- List all New Headlines")
    print("----------------------------------------------------")
    print("5- Back to Main Menu")
    print("----------------------------------------------------")
    lower_option = int(input("Enter your option: "))
    print("###################################################\n")
    if lower_option == 1:
        request = input("Enter a pecific keword you want to search about: ")
        option = f"1.{lower_option}.{request}"
        send_client(option, cs)
        headlines(cs)
    elif lower_option == 2:
        print(["entertainment","business" , "general", "technology","sports", "science" ,"health" ])
        request = input(f"\nEnter the desired category: ")
        if request not in cat:
            print("sorry, Invalid category choose from the list above")
            return
        option = f"1.{lower_option}.{request}"
        send_client(option, cs)
        headlines(cs)
    elif lower_option == 3:
        request = input(f"Enter country: ['eg', 'nz', 'ca', 'ae', 'sa', 'gb', 'us','au' , 'ma']")
        if request not in regions:
            print("sorry, Invalid country choose from the list above")
            return
        option = f"1.{lower_option}.{request}"
        send_client(option, cs)
        headlines(cs)
    elif lower_option == 4:
        option = f"1.{lower_option}.null"
        send_client(option, cs)
        headlines(cs)
    elif lower_option == 5:
        return
    else:
        print("Invalid option. Please chooce and option from the list above")
        return
def sources_menu(cs):
    print("Select the desired option: ")
    print("1- Search by category")
    print("----------------------------------------------------")
    print("2- Search by country")
    print("----------------------------------------------------")
    print("3- Search by languages")
    print("----------------------------------------------------")
    print("4- List all the available sources")
    print("----------------------------------------------------")
    print("5- Back to Main Menu")
    print("----------------------------------------------------")
    lower_option = int(input("Enter your option: "))
    print("###################################################\n")
    if lower_option == 1:
        request = input(f"Enter category: ['entertainment','business' , 'general', 'technology','sports', 'science' ,'health' ]")
        if request not in cat:
            print("sorry, Invalid category choose from the list above")
            return
        option = f"2.{lower_option}.{request}"
        send_client(option, cs)
        resources(cs)
    elif lower_option == 2:
        request = input(f"Enter country: ['eg', 'nz', 'ca', 'ae', 'sa', 'gb', 'us','au' , 'ma']")
        if request not in regions:
            print("sorry, Invalid country choose from the list above")
            return
        option = f"2.{lower_option}.{request}"
        send_client(option, cs)
        resources(cs)
    elif lower_option == 3:
        request = input(f"Enter language:['ar', 'en']")
        if request not in languages:
            print("sorry, Invalid language choose from the list above")
            return
        option = f"2.{lower_option}.{request}"
        send_client(option, cs)
        resources(cs)
    elif lower_option == 4:
        option = f"2.{lower_option}.null"
        send_client(option, cs)
        resources(cs)
    if lower_option == 5:
        return
    else:
        print("Invalid option. Please chooce and option from the list above")
        return


def headlines(cs):
    print("please wait we are processing you request:\n")
    headlines_data = cs.recv(200000).decode()
    list = json.loads(headlines_data)
    print("the reached headlines:\n")
    print("----------------------------------------------------")
    for index, item in enumerate(list['articles']):
        print(f"{index + 1}. {item['title']} - {item['description']}\n \n")
    headNo = int(input("Enter the article number that you want to its details: "))
    print("################################################################")
    desired_headline = list['articles'][headNo - 1]
    print(f"""Article {headNo} Details:
        Source: {desired_headline['source']['name']}
        ----------------------------------------------------
        Author: {desired_headline['author']}
        ----------------------------------------------------
        Title: {desired_headline['title']}
        ----------------------------------------------------
        URL: {desired_headline['url']}
        ----------------------------------------------------
        Description: {desired_headline['description']}
        ----------------------------------------------------
        Published At: {desired_headline['publishedAt']}
        """)
def resources(cs):
    print("please wait we are processing you request:\n")
    sources_data = cs.recv(200000)
    sources_data.decode()
    list = json.loads(sources_data)
    print("the reached sources:\n")
    print("----------------------------------------------------")
    for index, item in enumerate(list['sources']):
        print(f"{index + 1}. {item['name']}")
    sourceNO = int(input("Enter the source number that you want to access its details:  "))
    print("################################################################")
    desired_source = list['sources'][sourceNO - 1]
    print(f"""Source {sourceNO} Details:
        ----------------------------------------------------
        Source: {desired_source['name']}
        ----------------------------------------------------
        Country: {desired_source['country']}
        ----------------------------------------------------
        Description: {desired_source['description']}
        ----------------------------------------------------
        URL: {desired_source['url']}
        ----------------------------------------------------
        Category: {desired_source['category']}
        ----------------------------------------------------
        Language: {desired_source['language']}
        """)
def send_client(option, cs):
    cs.send(option.encode())

cat = ["entertainment","business" , "general", "technology","sports", "science" ,"health" ]
regions = ["eg", "nz", "ca", "ae", "sa", "gb", "us","au" , "ma"]
languages = ["ar", "en"]

if __name__ == "__main__":
    #starting the client
    main_menu()
