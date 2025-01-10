# Secure Message Encryption and Hashing
# Author: Eyong Christopher
# This script demonstrates how to use the cryptography module in Python for securely encrypting,
# decrypting, and hashing messages using symmetric encryption (AES with Fernet) and SHA-256.
#
# Requirements:
# - Python 3.x
# - cryptography module
#
# Instructions:
# 1. Install the required cryptography module:
#    pip install cryptography
#
# 2. Run the script:
#    python secure_message_encryption.py
#
# 3. Follow the prompts to:
#    - Encrypt a message by entering 'e'.
#    - Decrypt an encrypted message by entering 'd'.
#    - Hash a message using SHA-256 by entering 'h'.
#    - Exit the script by entering 'q'.

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as secret.key")

# Function to load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a message
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to hash a message using SHA-256
def hash_message(message):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(message.encode())
    return digest.finalize()

# Main function to interact with the user
def main():
    while True:
        action = input("Do you want to (e)ncrypt, (d)ecrypt, (h)ash a message, or (q)uit? ").lower()

        if action == "e":
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message)
            print("Encrypted message:", encrypted_message)
        elif action == "d":
            encrypted_message = input("Enter the encrypted message: ").encode()
            decrypted_message = decrypt_message(encrypted_message)
            print("Decrypted message:", decrypted_message)
        elif action == "h":
            message = input("Enter the message to hash: ")
            hashed_message = hash_message(message)
            print("SHA-256 Hash of the message:", hashed_message.hex())
        elif action == "q":
            break
        else:
            print("Invalid input. Please enter 'e', 'd', 'h', or 'q'.")

if __name__ == "__main__":
    # Check if secret.key exists, if not, generate it
    try:
        load_key()
    except FileNotFoundError:
        generate_key()
    
    main()
