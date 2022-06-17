from nordvpn_connect import *
import os
import socket

settings = initialize_vpn("Switzerland")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    if (get_ip() != "10.5.0.2"):
        rotate_VPN(settings)

if __name__ == "__main__":
    while True:
        main()
        time.sleep(5)
