import hashlib
import os

def build_merkle_tree(data):
    # Pas 1: Hash pentru fiecare element
    hashed_data = [hashlib.sha256(str(elem).encode()).hexdigest() for elem in data]

    print("=== Hash frunze (leaves) ===")
    for i, h in enumerate(hashed_data):
        print(f"Element {i}: {h}")
    print()

    # Pas 2: Build Merkle tree
    level = 1
    while len(hashed_data) > 1:

        if len(hashed_data) % 2 != 0:
            hashed_data.append(hashed_data[-1])

        new_level = []
        for i in range(0, len(hashed_data), 2):
            combined = hashed_data[i] + hashed_data[i + 1]
            new_hash = hashlib.sha256(combined.encode()).hexdigest()
            new_level.append(new_hash)

        hashed_data = new_level

        print(f"=== Nivel {level} ===")
        for h in hashed_data:
            print(h)
        print()

        level += 1

    return hashed_data[0]


folder = "date"
data_set = []

print("=== Hash pentru fiecare fisier ===")

for file in sorted(os.listdir(folder))[:4]:   
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            content = f.read().strip()
            file_hash = hashlib.sha256(content.encode()).hexdigest()
            print(f"{file} -> {file_hash}")
            data_set.append(content)

print()

root_hash = build_merkle_tree(data_set)
print("Hash Radacina (root):", root_hash)