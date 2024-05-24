import socket
import threading
import json
from newsapi import NewsApiClient

APIKEY = '844863c15fad42cba626fb66d2c24ef2'
magazine_api = NewsApiClient(api_key=APIKEY)

Server_host = "127.0.0.1"
port = 5349


# start server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((Server_host, port))
    server_socket.listen(3)
    print(f"Server is listening on {Server_host}:{port}")
    while True:
        cs, client_address = server_socket.accept()
        client_handler = threading.Thread(target=client_handling, args=(cs, client_address))
        client_handler.start()


# handeling the client request
def client_handling(cs, address):
    print(address, " is connected to the server")
    while True:
        username = cs.recv(2048).decode("utf-8")
        user_message = cs.recv(2048).decode("utf-8")
        if user_message == None:
            break
        head_option, sub_option,request = user_message.split(".")
        if head_option == '1':
            headlines(request, sub_option, username)
        elif head_option == '2':
            sources(request, sub_option, username)

    cs.close()


def headlines(request, option, client_name):
    if option == '1':
        data = magazine_api.get_top_headlines(q=request)
    elif option == '2':
        data = magazine_api.get_top_headlines(category=request)
    elif option == '3':
        data = magazine_api.get_top_headlines(country=request)
    elif option == '4':
        data = magazine_api.get_top_headlines()

    with open(f'A14{client_name}1.{option}.json', 'w') as outfile:
        json.dump(data, outfile)


def sources(request, option, client_name):
    if option == '1':
        data = magazine_api.get_sources(category=request)
    elif option == '2':
        data = magazine_api.get_sources(country=request)
    elif option == '3':
        data = magazine_api.get_sources(language=request)
    elif option == '4':
        data = magazine_api.get_sources()

    with open(f'A14{client_name}_2.{option}.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    start_server()
