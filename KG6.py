from Crypto.PublicKey import RSA

## Generate public/private RSA key pair
key = RSA.generate(2048)

## Save private key to file
priv_key = key.export_key()

with open("d.key", "wb") as file_out:
    file_out.write(priv_key)

## Save public key to file
pub_key = key.publickey().export_key()

with open("e.key", "wb") as file_out:
    file_out.write(pub_key)