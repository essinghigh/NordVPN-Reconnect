from nordvpn_connect import *
import os
from datetime import datetime as dt
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

def connect():
    rotate_VPN(settings)

def main():
    if (get_ip() != "10.5.0.2"):
        print("Debug: Disconnected")
        connect()
        time.sleep(10)
    else:
        print("Debug: Connected")
    time.sleep(5)


if __name__ == "__main__":
    while True:
        main()
