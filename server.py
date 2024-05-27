import socket
import threading
import json
import os

from newsapi import NewsApiClient

api = NewsApiClient(api_key='a86d8a517347451cb5335ce0b0f09bff')

def get_sources(request, lower_option, client_name):
    if lower_option == '1':
        data = api.get_sources(category=request)
    elif lower_option == '2':
        data = api.get_sources(country=request)
    elif lower_option == '3':
        data = api.get_sources(language=request)
    elif lower_option == '4':
        data = api.get_sources()
    data["sources"] = data["sources"][0:15]
    with open(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database"),
                            f'A14_{client_name}_2.{lower_option}.json'), 'w') as outfile:
        json.dump(data, outfile)

def get_headlines(request, lower_option, client_name):
    if lower_option == '1':
        data = api.get_top_headlines(q=request)
    elif lower_option == '2':
        data = api.get_top_headlines(category=request)
    elif lower_option == '3':
        data = api.get_top_headlines(country=request)
    elif lower_option == '4':
        data = api.get_top_headlines()
    data["articles"] = data["articles"][0:15]
    with open(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database"),
                            f'A14_{client_name}_1.{lower_option}.json'), 'w') as outfile:
        json.dump(data, outfile)
def StartupOfServer():
    ip_address = "127.0.0.1"
    port_number = 4926
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind((ip_address, port_number))
    ss.listen(3)
    print(f"Server is listening on...\n IP address: {ip_address} \n  Port number: {port_number}")
    while True:
        cs, Client_IP = ss.accept()
        client_handler = threading.Thread(target=client_handling, args=(cs, Client_IP))
        client_handler.start()
def client_handling(cs, address):
    print(f"Host {address} connected")
    username = cs.recv(8192).decode()
    print(f"Client {username} has connected to the server")
    while True:
        try:
            user_message = cs.recv(8192).decode()
            if not user_message:
                break
            upper_option, lower_option,request = user_message.split(".")
            if upper_option == "1":
                get_headlines(request, lower_option, username)
                data_extractionAndSending(upper_option, lower_option, username, cs)
            elif upper_option == "2":
                get_sources(request, lower_option, username)
                data_extractionAndSending(upper_option, lower_option, username, cs)

        except Exception as e:
            print(f"Error handling client {username}: {e}")
            break
    cs.close()
    print(f" {address} disconnected")
def data_extractionAndSending(upper_option, lower_option, username, cs):
    with open(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), "database"),
                           f'A14_{username}_{upper_option}.{lower_option}.json')) as f:
        records = json.load(f)
        cs.send(json.dumps(records).encode())
        print(f"A14_{username}_{upper_option}.{lower_option} has been delivered to {username} successfully")
if __name__ == "__main__":
    StartupOfServer()
