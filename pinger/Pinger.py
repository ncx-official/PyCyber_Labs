#!/usr/bin/env python3
# Automated ping using Python
# By Nasikovskyi Vitalii
# 02-01-2024

import ipaddress
import socket
import logging
import os
import platform
import argparse

def setup_logging(log_to_file=False, log_file='output.log'):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    if log_to_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        file_handler.setLevel(logging.INFO)
        logging.getLogger().addHandler(file_handler)

def validate_ip_address(text):
    try:
        ip_addr = ipaddress.ip_network(socket.gethostbyname(text))
        return str(ip_addr).split("/")[0]  # remove subnet mask
    except socket.gaierror as hostNameError:
        logging.error(f"The provided hostname could not be resolved. ({text})")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}.")
    return None

def read_file(name):
    result = []
    with open(name, 'r') as file:
        for string in file.read().split("\n"):
            result.append(string.lower().strip())

    logging.info(f'Reading IPs from {name}')
    return result

def send_ping_request(dest_ip, current_os):
    try:
        ping_command = f"ping -n 1 -w 2 {dest_ip} > nul" if current_os == "windows" else f"ping -c 1 -w {dest_ip} > /dev/null 2>&1"
        exit_code = os.system(ping_command)

        info_message = f"{dest_ip} is online" if exit_code == 0 else f"{dest_ip} is offline"
        logging.info(info_message)
    except OSError as e:
        logging.error(f"Error executing ping command: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return exit_code

def main():
    parser = argparse.ArgumentParser(description='Automated ping using Python.')
    parser.add_argument('--log', dest='log_to_file', action='store_true', help='Enable logging to a file')
    parser.add_argument('--log-file', dest='log_file', default='output.log', help='Specify the log file name')
    parser.add_argument('--file', dest='input_file', help='Specify the input file containing addresses to ping')
    parser.add_argument('ip_address', nargs='?', help='Specify a single IP address to ping')
    args = parser.parse_args()

    if args.log_to_file:
        setup_logging(log_to_file=True, log_file=args.log_file)
    else:
        setup_logging()

    if args.ip_address:
        # Check if a single IP address is provided
        single_ip = validate_ip_address(args.ip_address)
        if single_ip is not None:
            current_os = platform.system().lower()
            if current_os is not None:
                send_ping_request(dest_ip=single_ip, current_os=current_os)
        else:
            logging.error(f"Invalid IP address: {args.ip_address}")

    elif args.input_file:
        addresses_list = read_file(args.input_file)
        ip_addresses = [validate_ip_address(item) for item in addresses_list if validate_ip_address(item) is not None]

        logging.info(f'Imported {len(ip_addresses)} IPs')

        current_os = platform.system().lower()
        if current_os is not None:
            for ip in ip_addresses:
                send_ping_request(dest_ip=ip, current_os=current_os)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("User interrupted the program.")
