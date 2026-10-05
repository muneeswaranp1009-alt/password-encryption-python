# Password Encryption

A simple Python project showcasing the implementation of the Fernet symmetric encryption method of the cryptography library.

## Overview

The project can generate a secure encryption key utilizing the Fernet symmetric encryption method, take the input password, encrypt it, and display the encrypted password.

The project makes use of the cryptography and Python libraries.

## Implementation

1. Fernet encryption key is generated.

2. A Fernet encryption object is initialized with the generated key.

3. User is prompted for a password.

4. The given password is converted into a byte string.

5. The byte string is encrypted with the Fernet encryption object.

6. The encrypted password is output.

The project implements a Fernet encryption key with the help of `Fernet.generate_key()` and utilizes the encryption method of the Fernet object to encrypt the given string. :chart_with_upwards_trend{index="1"} The project showcases the basics of the Fernet symmetric key encryption.

The output of the project resembles the following:

Welcome to Encrypting

Secret key:

Enter Password to Encrypt:

Your Encrypted Password is:

The concepts practiced in the project include Python imports, user input, encryption, symmetric-key cryptography, Fernet, key generation, string encoding, and Python objects.

## Requirements Installation

Install the project requirements with the following command:

pip install cryptography

## Usage

1. Make sure Python is installed in your system.

2. Make sure to install the project requirements.

3. Save the code as the `Encryption.py` file.

4. Run the `Encryption.py` script:

python Encryption.py

5. Provide the password to be encrypted when prompted.

The project's file structure looks like this:

password-encryption-python/

│

├── Encryption.py

└── README.md

## Purpose

The project was created as a personal beginner Python project to learn and showcase the encryption concept and the implementation of the Fernet encryption method.

The potential future improvements for the project can include adding password decryption, saving and loading the encryption key, implementing a login system, file encryption, a graphical user interface, and key management.

## Author

The project was created as a learning Python project.
