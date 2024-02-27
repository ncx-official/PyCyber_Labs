import hashlib
import os

def create_hash(password, algorithm='sha256'):
    """Create a hash of a password."""
    # Convert the password to bytes
    password_bytes = password.encode()
    hash_obj = hashlib.sha256(password_bytes)
    # Return the hexadecimal representation of the digest
    return hash_obj.hexdigest()

def main():
    print("Password Hash Generator")
    password = input("Enter the password to hash: ")
    hash_result = create_hash(password)
    
    if hash_result:
        print(f"The hash for {password} is: {hash_result}")

if __name__ == "__main__":
    main()
