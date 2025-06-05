

# our server needs to do 2 things 
# (1) handle networking
# (2) handle encryption 

import socket
from cryptography.fernet import Fernet

# Load the same shared key as client
with open("key.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)


#set up the server to listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind(("0.0.0.0", 8080)) #think of this like "hey computer i wanna listen on this port"
server.listen(1)
print("Server is listening, waiting for a client to connect...")


#accept an incoming connection from a client.
conn, addr = server.accept()
print(f"Connection established with {addr}")


while True:
    #Receive & Decrypt Message
    encrypted_msg = conn.recv(4096)
    decrypted_msg = fernet.decrypt(encrypted_msg)
    print(f"[CLIENT]: {decrypted_msg.decode()}")

    #Reply Back to the Client
    msg = input("Send to client: ") 
    encryptmsg = fernet.encrypt(msg.encode())
    conn.send(encryptmsg)


