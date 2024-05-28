import bitcoin
import random

# Generate a random private key
private_key = 1
private_key = hex(private_key)[2:]
private_key = private_key.rjust(64,"0") 
decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
valid_private_key = 0 < decoded_private_key < bitcoin.N

file = open("WalletDetail.txt","a")

print ("Private Key (hex) is: ", private_key)
print ("Private Key (decimal) is: ", decoded_private_key)
Data = f"\nPrivate Key (Hex): {private_key}\nPrivate Key (Decimal): {decoded_private_key}\n"


# Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print ("Private Key (WIF) is: ", wif_encoded_private_key)
Data += f"\nPrivate Key (WIF) is: {wif_encoded_private_key}\n"


# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(private_key, 'hex'), 'wif_compressed')
print ("Private Key (WIF-Compressed) is: ", wif_compressed_private_key)
Data += f"\nPrivate Key (WIF-Compressed) is: {wif_compressed_private_key}\n"


# Multiply the EC generator point G with the private key to get a public key point
public_key = bitcoin.multiply(bitcoin.G, decoded_private_key)
print(public_key)


# Encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex')
print ("Public Key (hex) is:", hex_encoded_public_key)
Data += f"\nPublic Key (hex) is: {hex_encoded_public_key}\n"


# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
 compressed_prefix = '02'
else:
 compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print ("Compressed Public Key (hex) is:", hex_compressed_public_key)
Data += f"\nCompressed Public Key (hex) is: {hex_compressed_public_key}\n"


# Generate bitcoin address from public key
print ("Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(public_key))
Data += f"\nBitcoin Address (b58check) is: {bitcoin.pubkey_to_address(public_key)}\n"


# Generate compressed bitcoin address from compressed public key
print ("Compressed Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(hex_compressed_public_key))
Data += f"\nCompressed Bitcoin Address (b58check) is: {bitcoin.pubkey_to_address(hex_compressed_public_key)}\n"
file.write(Data)
file.close()
input("\t\t\t\t\tPress Any key to Exit ...")
