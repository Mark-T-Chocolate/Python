#!/usr/bin/python3
import os
import warnings
import sys
import socket
import ipaddress

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

remote_host = input ("Enter remote host ip address :")
remote_port = int(input("Enter remote host port :"))
ipaddress.ip_address(remote_host)
server_address = (remote_host,remote_port)
sock.connect(server_address)

values = ("This is my message I hope this works")
print(values)
binary = values.encode('utf-8')
print('sending {!r}'.format(binary))
sock.sendall(binary)

responsedata = sock.recv(4096)
response = bytearray(responsedata)
print(responsedata)

sock.close()