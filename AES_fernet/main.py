#!/usr/bin/env python3
# Automated ping using Python
# By Nasikovskyi Vitalii
# 02-01-2024

import sys
from crypto_service_utility import CryptoServiceUtility
import os

def main():
    # Define the actions for encryption and decryption
    actions = ['encrypt_text', 'decrypt_text', 'encrypt_file', 'decrypt_file']
    print(f"Available actions: {actions}")

    # Gather inputs from the user
    action = input("Enter action (encrypt_text, decrypt_text, encrypt_file, decrypt_file): ")
    password = input("Enter password for encryption/decryption: ")

    # Perform the chosen action
    try:
        if action == 'encrypt_text':
            text_to_encrypt = input("Enter text to encrypt: ")
            encrypted_text = CryptoServiceUtility.encrypt_text(text_to_encrypt, password)
            print(f"Encrypted text: {encrypted_text}")

        elif action == 'decrypt_text':
            text_to_decrypt = input("Enter text to decrypt: ")
            decrypted_text = CryptoServiceUtility.decrypt_text(text_to_decrypt, password)
            print(f"Decrypted text: {decrypted_text}")

        elif action == 'encrypt_file':
            file_path = input("Enter the path of the file to encrypt: ")
            save_file_path = input("Enter the full path where you want to save the encrypted file (including file name): ")
            # Ensure directory exists
            save_dir = os.path.dirname(save_file_path)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            CryptoServiceUtility.encrypt_file(file_path, password, save_file_path)
            print(f"File encrypted successfully and saved to {save_file_path}")

        elif action == 'decrypt_file':
            encrypted_file_path = input("Enter the path of the encrypted file: ")
            save_file_path = input("Enter the full path where you want to save the decrypted file (including file name): ")
            # Ensure directory exists
            save_dir = os.path.dirname(save_file_path)
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            CryptoServiceUtility.decrypt_file(encrypted_file_path, password, save_file_path)
            print(f"File decrypted successfully and saved to {save_file_path}")

        else:
            print("Invalid action. Please choose from the available actions.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()