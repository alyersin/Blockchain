import hashlib
import os

def build_merkle_tree(data):
    # Pas 1: Hash pentru fiecare element
    hashed_data = [hashlib.sha256(str(elem).encode()).hexdigest() for elem in data]

    # Pas 2: Build Merkle tree
    while len(hashed_data) > 1:

        if len(hashed_data) % 2 != 0:
            hashed_data.append(hashed_data[-1])

        hashed_data = [
            hashlib.sha256((hashed_data[i] + hashed_data[i + 1]).encode()).hexdigest()
            for i in range(0, len(hashed_data), 2)
        ]

    return hashed_data[0]



folder = "date"
data_set = []

for file in sorted(os.listdir(folder))[:4]:
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            content = f.read().strip()
            data_set.append(content)

root_hash = build_merkle_tree(data_set)
print("Hash Radacina (root):", root_hash)