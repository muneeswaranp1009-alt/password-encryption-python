from cryptography.fernet import Fernet

create_key = Fernet.generate_key()

key = Fernet(create_key)

print("\nWelcome to Encrypting")

print(f"\nSecret key({create_key.decode()})")

get_input = input("\nEnter Password to Encrypt:")

encrypt = key.encrypt(get_input.encode())

print(f"\nYour Encrypted Password is {encrypt}")

