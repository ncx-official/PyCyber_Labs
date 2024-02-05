# Python for Cybersecurity Labs

## Automated Ping Tool with Python

A simple and efficient command-line tool for automated ping using Python. Developed as part of a college lab exercise, this script allows you to check the online or offline status of multiple IP addresses quickly.

### Features:
- Automated Ping: Ping multiple IP addresses effortlessly.
- Logging: Option to log results to a file for future reference.
- Input Options: Support for single IP address input and reading IP addresses from a file.

### Usage:
Single IP Address:
```
python pinger.py 192.168.1.1
```
IP Addresses from File:
```
python pinger.py --file addresses.txt
```
Logging to a File:
```
python pinger.py --log --file addresses.txt
```

### Requirements:
Python 3.x
Platform: Windows/Linux

Feel free to use and modify this script according to your needs. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request!

#

## Port Scanner Script

This Python script utilizes the nmap library to scan ports on a specified target IP address. It provides the flexibility to scan a single port or a range of ports.

### Installation
```
pip install python-nmap
```

### Usage
```
python script_name.py <target_ip> <ports>
```

```
python script_name.py 127.0.0.1 80
```

To scan a range of ports:

```
python script_name.py 127.0.0.1 75-125
```