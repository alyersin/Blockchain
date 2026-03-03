import hashlib

def build_merkle_tree(data):
    # Pas  1: Hash pentru fiecare element
    hashed_data = [hashlib.sha256(str(elem).encode()).hexdigest() for elem in data]

    # Pas 2: Build  Merkle tree
    while len(hashed_data) > 1:
        hashed_data = [hashlib.sha256((hashed_data[i] + hashed_data[i + 1]).encode()).hexdigest() for i in range(0, len(hashed_data), 2)]

    return hashed_data[0]

# Exemplu de utilizare
data_set = ["Transactia1", "Transactia2", "Transactia3", "Transactia4", "Transactia5", "Transactia6", "Transactia7", "Transactia8"]
root_hash = build_merkle_tree(data_set)
print("Hash Radacina ( root):", root_hash)