import socket
port = 67 # this is the dedicated dhcp server request socket 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #sets socket as internet ipv4 (af_inet) , SOCK_DGRAM = UDP connection   
s.bind(("", port)) # UDP since theres no device ip. just listens to the port
print("waiting on port:", port)
while 1:
    data, addr = s.recvfrom(342)#number is the number of bytes
    print("someone is attempting to connect")
    


