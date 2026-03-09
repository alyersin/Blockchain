from mnemonic import Mnemonic
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import base58
from btclib import bip32

# Generare 12 cuvinte menomica
mnemonic_words = Mnemonic("english").generate(strength=128)

# Seed din fraza menmonica
seed_bytes = Mnemonic("english").to_seed(mnemonic_words)

# Private Key
master_private_key = bip32.rootxprv_from_seed(seed_bytes)

# DPublic Key
master_public_key = bip32.xpub_from_xprv(master_private_key)

# Base58 private key
decoded_private_key = base58.b58decode(master_private_key)

# Eliminare prefix
private_key_bytes = decoded_private_key[1:]

# Truncare sau adaugare octeti  private key la 32 bytes
private_key_bytes = private_key_bytes.ljust(32, b'\x00')[:32]

# Semnare obiect
sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)

# Verificare semnatura
vk = sk.verifying_key

# Base58 public key
decoded_public_key = base58.b58decode(master_public_key)

# Eliminare octet prefix 
public_key_bytes = decoded_public_key[1:]

# Mesajul de intrare
message = "Acesta este un mesaj de semnat!"

# Semnare mesaj cu Private Key
signature = sk.sign(message.encode())

# Verificare semnatura cu Public Key
verification_result = vk.verify(signature, message.encode())

# Afisare rezultat
print("Mnemonica:", mnemonic_words)
print("Private Key:", master_private_key)
print("Public Key:", master_public_key)
print("Semnatura:", signature.hex())
print("Verificare rezultat:", verification_result)
