import socket
import json

cat = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
country = ["au", "nz", "ca", "ae", "sa", "gb", "us", "eg", "ma"]
language = ["ar", "en"]


def send(option, cs):
    cs.send(option.encode("utf-8"))


def main_menu(cs):
    print("1.Search headlines\n")
    print("2.List of scources\n")
    print("3.Quit\n")
    option = int(input("Choose an option = \n"))
    if option == 1:
        headline_search(cs)
    if option == 2:
        list_of_sources(cs)
    if option == 3:
        cs.close()
    else:
        print("Invalid Option")
        return


def headline_search(cs):
    print("1.Search for keywords\n")
    print("2.Search by category\n")
    print("3.Search by country\n")
    print("4.List all new headlines\n")
    print("5.Back to main menu\n")
    option = input("Choose an option = \n")
    if option == 1:
        criteria = input("Enter keyword: \n")
        msg = f"1.{option}.{criteria}\n"
        send(msg, cs)
    if option == 2:
        criteria = input("Enter category: (business, entertainment, general, health, science, sports, technology) = \n")
        if criteria not in cat:
            print("Invalid Option")
            return
        msg = f"1.{option}.{criteria}\n"
        send(msg, cs)
    if option == 3:
        criteria = input("Enter country code: (au, nz, ca, ae, sa, gb, us, eg, ma) = \n")
        if criteria not in country:
            print("Invalid Option")
            return
        msg = f"1.{option}.{criteria}\n"
        send(msg, cs)
    if option == 4:
        msg = f"1.{option}\n"
        send(msg, cs)
    if option == 5:
        main_menu(cs)
    else:
        print("Invalid Option")
        return
    recieve_headline(cs)
    return


def list_of_sources(cs):
    print("1.Search by category\n")
    print("2.Search by country\n")
    print("3.Search by language\n")
    print("4.List all\n")
    print("5.Back to the main menu\n")
    option = input("Choose an option = \n")
    if option == 1:
        criteria = input("Enter category: (business, entertainment, general, health, science, sports, technology) = \n")
        if criteria not in cat:
            print("Invalid Option")
            return
        msg = f"2.{option}.{criteria}\n"
        send(msg, cs)
    if option == 2:
        criteria = input("Enter country code: (au, nz, ca, ae, sa, gb, us, eg, ma) = \n")
        if criteria not in country:
            print("Invalid Option")
            return
        msg = f"2.{option}.{criteria}\n"
        send(msg, cs)
    if option == 3:
        criteria = input("Enter language code: (ar,en) = \n")
        if criteria not in language:
            print("Invalid Option")
            return
        msg = f"2.{option}.{criteria}\n"
        send(msg, cs)
    if option == 4:
        msg = f"2.{option}\n"
        send(msg, cs)
    if option == 5:
        main_menu(cs)
    else:
        print("Invalid Option")
        return
    recieve_scources(cs)
    return


def recieve_headline(cs):
    print("Recieving headlines please wait ...")
    headline_D = cs.recv(100000).decode("utf-8")
    headline_L = json.loads(headline_D)
    print("Recieved headline data :-")
    for i, item in enumerate(headline_L['articles']):
        print(f"{i + 1}. {item['title']} - {item['description']}")
    sel = int(input("Enter the article number = \n"))
    sel_headline = headline_L['articles'][sel-1]
    print(f"Article {sel} Details:")
    print(f"Source: {sel_headline['source']['name']}")
    print(f"Author: {sel_headline['author']}")
    print(f"Title: {sel_headline['title']}")
    print(f"URL: {sel_headline['url']}")
    print(f"Description: {sel_headline['description']}")
    print(f"Published At: {sel_headline['publishedAt']}")
    print(f"Content: {sel_headline['content']}")


def recieve_scources(cs):
    print("Receiving Sources please wait ...")
    source_D = cs.recv(100000).decode
    source_L = json.loads(source_D)
    print("Recieved Sources data :-")
    for i, item in enumerate(source_L['sources']):
        print(f"{i+1}.{item['name']}")
    sel = int(input("Enter the source number ="))
    sel_source = source_L['sources'][sel-1]
    print(f"Article {sel} Details:")
    print(f"Source: {sel_source['source']['name']}")
    print(f"Author: {sel_source['author']}")
    print(f"Title: {sel_source['title']}")
    print(f"URL: {sel_source['url']}")
    print(f"Description: {sel_source['description']}")
    print(f"Published At: {sel_source['publishedAt']}")
    print(f"Content: {sel_source['content']}")


def start_client():
    print("---------- Welcome to news API ----------\n")
    print("Connecting to server ..\n")
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(("127.0.0.1", 5349))
    print("----------Server Connected Successfully ----------\n")
    user_name = input("Enter your username: \n")
    cs.send(user_name.encode("utf-8"))
    main_menu(cs)


if __name__ == "__main__":
    start_client()
