import socket

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0

target_ip = input("Enter the target IP address: ")
port_range = range(1, 1025)  # Scan common ports from 1 to 1024

for port in port_range:
    if scan_port(target_ip, port):
        print(f"Port {port} is open")