from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import *
import sys

## Hardcoded private key
hardcoded_key = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAwso9Fyb5gkO73dh3BdLyEL3DcOIoPVlXI2ntyIfYOkzoQWWi8Z98rBznNGRc8K1kzqNbZRek+p6pdTo6+3j+JuZwZQ02YaQl5+TXpXF7CnG7kF4gUvrQRcRo4b90JURSrcYDU5XLtAD1g7VYtntN3LKKIRk+eovVCuSutH4sk7mR1tD1HNYLDbKrBtcWIpQlXCnRV07nRI4PQdno4W+ZZgFewD6cMCScDKBYN/Q1Y/cUs8xAGbx9WCKAEKJW2YgfQjndimz805n3A2L9cE3MvA7gtXBLedOtJnt9GJmTAdaoN35nWxnK86DEwc9ZPxoxcJMqKVxMgEW62t1jKDJImQIDAQABAoIBAA/paFMfVmtrMAn/uD1MDYULk08B0mqshR859HgYjLO6e5B4Bnb5YbxHgiV3+1WXvG/azUj1RP9J/aq7Tn0jVZOE6HKAwUv5ljUarvjvS68/OiShY7+TiHbig/TI6Gpw6dYTIktuJZ03JNcU9cG2UdZw6TKp9r4Y9Ra2NoU891Q7xE1A5p13/jLB8kSLD527EHLpIPL+f18wqoNV3UgpOAHXKoR1oP7/3fEDZTTG5jSkd/QI2PLYfYb4VlVNHTyPtYIKmCSix0UCJBUuDbpty2aiP8wXKJZtkiX7hqTZHvYjBsDbiVoXRWY3k6McFYyuoGxKHcx+iezSILvlpyb44VcCgYEAzOPINZPOAF7bBj4DsWqbkgq6TeXmumMS86yobhkGzKySYQgLTh0pRgl8fNUH19D7C6yv52fxQZ/2Tj96TlN3wrbuI/fH3/QcRjogyxVHUhmerM+E446C8pqK1LGgS5JPKBogekr0k0ES+yFHsAre+08RUGpGizGiISdMDjRGt5sCgYEA82F8ns8tTw1r+kMDD8EADPKI42Lld83x56COYv3Y51tXTbDsxhga4CTJ5gq3PT8T0ht3olOqLCHcCP8pM/uhRjNZ91geOCn/XzD4zHQnOCtWYjf6uTUqHG4Rk0WtzjnB2Fi+lR4UK6XJi23nGbW3m6evm/uPYxYRAhDL7pDildsCgYAaHtPwWKaDj5Q2qINKBABPTwTPV4bhri3FWPakCpa+UyXaLu9aBwezARSYyYPVdLP8mghW5P5x0lXRRfBuud9juHSFq1oU6AcOwOxbV5wfEFsVRuN3KzzwdtlKIlcAK2fiAeqwDIw/laU41NZR0CD7Quo/KT1TE4HK3jqo+OsnDwKBgGWs/XYPEVusPMbhhf7n31CJZlywbTL+y6e7sKB0clA9HZzsZA5h9aBcXiiHo4OnvW0SYoljMH2da6IqjxkTb423WEd3/a/zA6fN+rLXd6cEm+MOheUn677S0O7YtkKoaG4srPn5Be4yJZ/lOx3Hh7w0cq3Ui1OW3WYihD/XMYHvAoGANY1PIEcKusSKnZlT70mV2zQ4xnyMk41XC89EMlvW2e4XEAEQBgrLNhvfYnk46+ikG7JLYq2sYbYmUSaSDT35wSviewD9GHJWl7Rs1Zoau9gXC91QPIOWlEHxPTRowKD2ZAowU71855pCMPWbR6OuwUqtrTzDhvidpqqQ22xCQYM=\n-----END RSA PRIVATE KEY-----"

## Put key in readable format by RSA decryption object
private_key = RSA.import_key(hardcoded_key)

## Stop program if unique identifier is not provided as a parameter
if len(sys.argv) != 2:
    print("Please enter the unique identifier as a parameter.")
    sys.exit(1)

## Read the identifier into variable
enc_session_key = b64decode(sys.argv[1])

## Decrypt identifier into AES key to use for file decryption
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

## Print file key to stdout in human readable text
print(b64encode(session_key).decode())