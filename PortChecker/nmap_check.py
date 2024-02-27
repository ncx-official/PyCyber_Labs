#!/usr/bin/env python3
# Open ports checker using Python (NMAP API)
# By Nasikovskyi Vitalii
# Date: 02-04-2024

import argparse
import nmap
import ipaddress

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port_range(port_range):
    if '-' in port_range:
        start, end = map(int, port_range.split('-'))
        if start < 0 or end > 65535 or start > end:
            raise argparse.ArgumentTypeError("Port range must be 0-65535 and start must be less than end.")
    else:
        port = int(port_range)
        if port < 0 or port > 65535:
            raise argparse.ArgumentTypeError("Port must be between 0 and 65535.")
    return port_range

def scan_ports(target_ip, ports):
    scanner = nmap.PortScanner()

    try:
        if '-' in ports:
            start, end = map(int, ports.split('-'))
            port_range = f"{start}-{end}"
        else:
            start, end = int(ports), int(ports)  # Single port case
            port_range = ports

        # Perform the scan
        result = scanner.scan(target_ip, port_range, arguments='-Pn')  # '-Pn' skips host discovery

        # Check if the IP address is in the results
        if target_ip not in result['scan']:
            print(f"No information available for IP: {target_ip}. It might be down or blocking nmap scans.")
            return

        # Iterate over the entire range of specified ports
        for port in range(start, end + 1):
            if 'tcp' in result['scan'][target_ip] and port in result['scan'][target_ip]['tcp']:
                # If the port is in the results, print its state
                print(f"Port {port} is {result['scan'][target_ip]['tcp'][port]['state']}.")
            # else:
                # If the port is not in the results, assume it was not scanned or is closed
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='Scan ports on a target IP.')
    parser.add_argument('target_ip', type=str, help='Target IP address to scan.', 
                        metavar='IP', action='store')
    parser.add_argument('ports', type=validate_port_range, 
                        help='Port or port range to scan. Use "-" for a range (e.g., 20-80).',
                        metavar='PORTS', action='store')

    args = parser.parse_args()

    if validate_ip(args.target_ip):
        scan_ports(args.target_ip, args.ports)
    else:
        print("Invalid IP address format.")

if __name__ == "__main__":
    main()