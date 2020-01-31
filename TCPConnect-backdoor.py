import socket
import subprocess
target_ip = raw_input("Target ip :")
port = 4554
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.connect((target_ip,port))
print (s.recv(1024))
while True:
    command = raw_input("Shell>>")
    if command == 'exit':
        print ("[-]See you Later Mustafa...")
        break

    else:
        s.send(command)
        print (s.recv(1024))
