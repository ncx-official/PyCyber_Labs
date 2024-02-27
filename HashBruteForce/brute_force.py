import argparse
import hashlib
import os

# Load the dictionary
def load_dictionary(file_path):
    # Check if the file path exists
    if not os.path.exists(file_path):
        print(f"Error: The file path {file_path} does not exist.")
        exit(1)  # Exit the script if the file does not exist
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Attempt to crack the hash
def crack_hash(hash_to_crack, dictionary):
    for word in dictionary:
        # Hash the word using the same algorithm as the original hash
        attempted_hash = hashlib.sha256(word.encode()).hexdigest()
        if attempted_hash == hash_to_crack:
            return word
    return None

# Main function to set up the cracking process
def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Crack an unsalted hash using a provided dictionary of common passwords.")
    parser.add_argument("hash", help="The hash to attempt to crack.")
    parser.add_argument("passwords_dict", help="File path to the dictionary of common passwords.")
    args = parser.parse_args()

    # Check if the provided dictionary file exists
    if not os.path.exists(args.passwords_dict):
        print(f"Error: The file {args.passwords_dict} does not exist.")
        exit(1)

    # Load dictionary
    common_passwords = load_dictionary(args.passwords_dict)
    
    # Attempt to crack the hash using the dictionary
    cracked_password = crack_hash(args.hash, common_passwords)
    
    if cracked_password:
        print(f"Success! The password is: {cracked_password}")
    else:
        print("Failed to crack the hash.")

if __name__ == "__main__":
    main()
