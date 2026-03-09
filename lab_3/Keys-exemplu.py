from ecdsa import SigningKey, VerifyingKey, SECP256k1
import base58

# Define the child private and public keys
child_private_key_b58 = "xprv9vGwnKiQPwqufYpchdN4SkDDz9teSfXWTHDWDNPn8ikXYUneWYpLWq8WtAxRyiUqgvcAZh2LoVQK8XuuZtLVNjFtFVH1BkkG2hhqFkb2VdK"
child_public_key_b58 = "xpub69GJBqFJEKQCt2u5oeu4ot9xYBj8r8FMpW971koPh4HWRH7o468b4dSzjTusfrEVNxMYrc1CCdbn6Le1zeSsJpKQaJRYrFJezW56P9V6GmR"

# Decode Base58 private key
decoded_private_key = base58.b58decode(child_private_key_b58)

# Remove the prefix byte
private_key_bytes = decoded_private_key[1:]

# Pad or truncate the private key bytes to 32 bytes
private_key_bytes = private_key_bytes.ljust(32, b'\x00')[:32]

# Create the SigningKey object
sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)

# Derive the VerifyingKey object from the private key
vk = sk.verifying_key

# Decode Base58 public key
decoded_public_key = base58.b58decode(child_public_key_b58)

# Remove the prefix byte
public_key_bytes = decoded_public_key[1:]

# Message to sign
message = "Hello, world!"

# Sign the message using the private key
signature = sk.sign(message.encode())

# Verify the signature using the public key
verification_result = vk.verify(signature, message.encode())

# Print the results
print("Signature:", signature.hex())
print("Verification Result:", verification_result)
