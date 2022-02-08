from nordvpn_connect import *
import os
import socket

# Switzerland numero uno
settings = initialize_vpn("Switzerland")

# NordLynx Local IP = 10.5.0.2, so if this does not return that then something is wrong
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

# This isn't really supposed to be used for intiial connection, but it works
def connect():
    rotate_VPN(settings)

# Change as neccessary for OpenVPN Protocols
def main():
    if (get_ip() != "10.5.0.2"):
        print("Debug: Disconnected")
        connect()
        time.sleep(10) # Just in-case it takes NordVPN a little to connect
    else:
        print("Debug: Connected")
    time.sleep(5)


if __name__ == "__main__":
    while True:
        main()
