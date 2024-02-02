#!/usr/bin/env python3
# Automated ping using Python
# By Nasikovskyi Vitalii
# 02-01-2024

import ipaddress
import socket
import datetime

def validate_ip_address(text):
    try:
        ip_addr = ipaddress.ip_network(socket.gethostbyname(text))
        return ip_addr
    except socket.gaierror as hostNameError:        
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Error: {hostNameError}. The provided hostname could not be resolved.")
    except Exception as e:
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - An unexpected error occurred: {e}.")
    return None

def main():
    print(f"\n{validate_ip_address(input('Enter IP: '))}")

if __name__ == "__main__":
    main()