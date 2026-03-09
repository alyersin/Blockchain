from bitcoinlib.keys import HDKey
import mnemonic

def generate_bip32_wallet(mnemonic_words):
    seed = mnemonic.Mnemonic.to_seed(mnemonic_words)
    hd_key = HDKey.from_seed(seed)
    root_key = hd_key.child_private(0)
    print("Master Address (BIP32):", root_key.address())
    print("Master Private Key (BIP32):", root_key.wif())

def main():
    mnemonic_words = "abandon ability able about above absent absorb abstract absurd abuse access accident"
    generate_bip32_wallet(mnemonic_words)

if __name__ == "__main__":
    main()
