from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import *
import os, sys

## Stop program if encrypted filename is not provided as a parameter
if len(sys.argv) != 2:
    print("Please provide the encrypted filename as the parameter")
    sys.exit(1)

## Read the encrypted filename into a variable
filename = sys.argv[1]

## Read the IV and encrypted data in from the encrypted file
file_in = open(filename, 'rb')
iv = file_in.read(16)
encrypted_data = file_in.read()
file_in.close()

## Have the user input the key that they were provided from the hacker
session_key = b64decode((bytes(input("Enter the key that you were provided with: ").encode())))

## Decrypt the file data using the inputted key
cipher_aes = AES.new(session_key, AES.MODE_CBC, iv)
data = unpad(cipher_aes.decrypt(encrypted_data), AES.block_size)

## Write the decrypted data to a file for the user to have
file_out = open(filename.replace('.encrypted', ''), 'wb')
file_out.write(data)
file_out.close

## Remove any excess files that were created during encryption
os.remove(filename.replace('.encrypted', '.ID'))
os.remove(filename.replace('.encrypted', '.note'))
os.remove(filename)