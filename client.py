import socket

print("---------- Welcome to news API ----------")
user_name = input("Please enter your username: ")
print("Conecting to server ..")
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(("127.0.0.1",5349))
print("---------- Server Connected Successfully ----------")
