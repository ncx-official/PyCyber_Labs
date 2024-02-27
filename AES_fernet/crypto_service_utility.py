import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class CryptoServiceUtility:
    @staticmethod
    def generate_key(password):
        """Generate a 32-byte encryption key from the provided user password."""
        salt = os.urandom(16)  # Generate a random 16-byte (128-bit) salt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # Derive a 32-byte (256-bit) key
            salt=salt,
            iterations=480000,  # Number of iterations for the PBKDF2 algorithm
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key, salt

    @classmethod
    def encrypt_text(cls, text, password):
        """Encrypt text."""
        key, salt = cls.generate_key(password)
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())  # Encrypt the text
        # Prepend the salt to the encrypted data before converting to hex
        return (salt + encrypted_text).hex()

    @classmethod
    def encrypt_file(cls, file_path, password, save_file_path):
        """Encrypt a file."""
        with open(file_path, 'rb') as file:
            file_data = file.read()
        
        key, salt = cls.generate_key(password)
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(file_data)

        with open(save_file_path, 'wb') as encrypted_file:
            encrypted_file.write(salt + encrypted_data)  # Write salt followed by encrypted data

    @staticmethod
    def recreate_key(password, salt):
        """Recreate the encryption key from the password and salt."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    @classmethod
    def decrypt_text(cls, text, password):
        """Decrypt text."""
        encrypted_text_bytes = bytes.fromhex(text)  # Convert from hex to bytes
        salt, encrypted_text = encrypted_text_bytes[:16], encrypted_text_bytes[16:]  # Extract salt and encrypted data
        key = cls.recreate_key(password, salt)
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()  # Decrypt the text
        return decrypted_text

    @classmethod
    def decrypt_file(cls, encrypted_file_path, password, save_file_path):
        """Decrypt a file."""
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        salt, encrypted_data = encrypted_data[:16], encrypted_data[16:]  # Extract salt and encrypted data
        key = cls.recreate_key(password, salt)
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        with open(save_file_path, 'wb') as original_file:
            original_file.write(decrypted_data)