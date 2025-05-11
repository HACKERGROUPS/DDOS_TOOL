import socket

domain = input("Enter domain name: ")

try:
    ip_address = socket.gethostbyname(domain)
    print(f"Here is ip: {domain}: {ip_address}")
except socket.gaierror:
    print(f"ERROR: {domain}")

