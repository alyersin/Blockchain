import hashlib
import mnemonic

def generate_mnemonic(putereBiti=128):
    bytesEntropy = hashlib.sha256(b'Acest text este o entropie').digest()
    hexEntropy = bytesEntropy.hex()
    print("Entropia generata (in hex):", hexEntropy)

    #Conversie entropie in me=nemonica
    mnemo = mnemonic.Mnemonic('english')
    cuvantMnemonica = mnemo.to_mnemonic(bytesEntropy)
    print("Mnemonica generata:", cuvantMnemonica)

    return cuvantMnemonica

def validareMnemonica(cuvantMnemonica):
    mnemo = mnemonic.Mnemonic('english')
    if mnemo.check(cuvantMnemonica):
        print("Mnemonica este valida.")
    else:
        print("Mnemonica nu este valida..")

def main():
    # Generare mnemonica
    print("Generare Mnemonica ...")
    cuvantMnemonica = generate_mnemonic()

    # Validare Mnemonica generata
    print("\nValidare Mnemonica ...")
    validareMnemonica(cuvantMnemonica)

if __name__ == "__main__":
    main()
