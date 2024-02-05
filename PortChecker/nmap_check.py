#!/usr/bin/env python3
# Open ports checker using Python (NMAP API)
# By Nasikovskyi Vitalii
# 02-04-2024

import argparse
import nmap

def scan_ports(target_ip, ports):
    scanner = nmap.PortScanner()
    
    if '-' in ports:
        start, end = map(int, ports.split('-'))
        port_range = range(start, end + 1)
    else:
        port_range = [int(ports)]

    for port in port_range:
        result = scanner.scan(target_ip, str(port))
        print(f"Port {port} is {result['scan'][target_ip]['tcp'][port]['state']}.")

def main():
    parser = argparse.ArgumentParser(description='Scan ports on a target IP.')
    parser.add_argument('target_ip', help='Target IP address to scan.')
    parser.add_argument('ports', help='Port or port range to scan. Use "-" for a range (e.g., 75-125).')

    args = parser.parse_args()

    target_ip = args.target_ip
    ports = args.ports

    scan_ports(target_ip, ports)

if __name__ == "__main__":
    main()