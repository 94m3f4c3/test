import socket

hostname = socket.gethostname()

ipaddr = socket.gethostbyname(hostname)

print("Your name is " + hostname)

print("your ip address is " + ipaddr)