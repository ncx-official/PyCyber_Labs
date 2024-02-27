#!/usr/bin/env python3
# Caesar Cipher using Python
# By Nasikovskyi Vitalii
# 02-06-2024

import argparse
# ascii decimal table
# 26 - letters in the alphabet
# "a-z" -> between (97 - 122)
# "A-Z" -> between (65 - 90)
# "0-9" -> between (48 - 57)

def encrypt_text(text, shift, include_uppercase=False, include_numbers=False):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97) # lowercase
        elif include_uppercase and 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65) # uppercase
        elif include_numbers and '0' <= char <= '9':
            encrypted_text += chr((ord(char) - 48 + shift) % 10 + 48) # digits
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_text(text, shift, include_uppercase=True, include_numbers=False):
    return encrypt_text(text, -shift, include_uppercase, include_numbers)

def main():
    # Set up argument parsing for different use cases
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text using Caesar Cipher.')
    parser.add_argument('-t', '--text', type=str, help='Text to be encrypted or decrypted')
    parser.add_argument('-s', '--shift', type=int, help='Shift for the Caesar Cipher')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the text instead of encrypting')
    parser.add_argument('--include_uppercase', action='store_true', help='Include uppercase letters in the cipher')
    parser.add_argument('--include_numbers', action='store_true', help='Include numbers in the cipher')
    args = parser.parse_args()

    if args.decrypt:
        result = decrypt_text(args.text, args.shift, args.include_uppercase, args.include_numbers)
    else:
        result = encrypt_text(args.text, args.shift, args.include_uppercase, args.include_numbers)
    print(result)

if __name__ == "__main__":
    main()