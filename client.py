import socket

def start_client():
    print("---------- Welcome to news API ----------")
    print("Conecting to server ..")
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect(("127.0.0.1",5349))
    print("----------Server Connected Successfully ----------")
    user_name = input("Enter your username: ")
    cs.send(user_name.encode("utf-8"))

if __name__ == "__main__":
    start_client()
