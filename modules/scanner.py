import socket
import threading

def scan(address):
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        result = s.connect_ex((address, port))
        if result == 0:
            print(f"[>] Port {port} ... OPEN")
        elif result == 111:
            print(f"[>] Port {port} ... CLOSED")
        elif result in (110, 11):
            print(f"[>] Port {port} ... FILTERED/NO RESPONSE")
        else:
            print(f"[>] Port {port} ... ERROR ({result})")
        s.close()



