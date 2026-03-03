import os
import hashlib
from typing import List, Dict


class MerkleNode:
    def __init__(self, hash_value: str):
        self.hash = hash_value
        self.left = None
        self.right = None


class MerkleTree:
    def __init__(self, file_hashes: List[str]):
        self.root = self._build_tree(file_hashes)

    @staticmethod
    def _hash_file(file_path: str) -> str:
        """Generează hash-ul SHA-256 al unui fișier."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):  # Citim în bucate de 8KB
                hasher.update(chunk)
        return hasher.hexdigest()

    @staticmethod
    def _combine_hashes(hash1: str, hash2: str) -> str:
        """Combine două hash-uri folosind MD5."""
        combined = hash1 + hash2
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()

    def _build_tree(self, hashes: List[str]) -> MerkleNode:
        """Construiește arborele Merkle recursiv."""
        if len(hashes) == 0:
            return None
        if len(hashes) == 1:
            return MerkleNode(hashes[0])

        new_level_hashes = []
        for i in range(0, len(hashes), 2):
            left_hash = hashes[i]
            right_hash = hashes[i + 1] if i + 1 < len(hashes) else left_hash
            combined_hash = self._combine_hashes(left_hash, right_hash)
            new_level_hashes.append(combined_hash)

        parent_level = self._build_tree(new_level_hashes)
        return parent_level

    def get_root_hash(self) -> str:
        """Returnează hash-ul rădăcinii arborelui."""
        return self.root.hash if self.root else None


def generate_merkle_tree_from_folder(folder_path: str) -> MerkleTree:
    """Generează un Merkle Tree din fișierele dintr-un folder."""
    file_hashes = []
    file_list = sorted(os.listdir(folder_path))  # Sortăm fișierele pentru consistență

    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_hash = MerkleTree._hash_file(file_path)
            file_hashes.append(file_hash)

    return MerkleTree(file_hashes)


def verify_file_integrity(tree: MerkleTree, folder_path: str, file_name: str) -> bool:
    """Verifică integritatea unui fișier specific din arbore."""
    file_path = os.path.join(folder_path, file_name)
    if not os.path.isfile(file_path):
        print(f"Fișierul {file_name} nu există în folder.")
        return False

    file_hash = MerkleTree._hash_file(file_path)

    # Recalculăm Merkle Tree cu toate fișierele din folder
    recalculated_tree = generate_merkle_tree_from_folder(folder_path)
    recalculated_root_hash = recalculated_tree.get_root_hash()

    # Comparam hash-ul rădăcinii original cu cel recalculat
    return tree.get_root_hash() == recalculated_root_hash


# MAIN
if __name__ == "__main__":
    # Configurați folderul și fișierul de test
    folder_path = "./"  # Schimbați cu calea reală a folderului
    file_to_check = "sha256.js"  # Schimbați cu numele fișierului pe care doriți să-l verificați

    # Generăm Merkle Tree inițial
    merkle_tree = generate_merkle_tree_from_folder(folder_path)
    print(f"Hash-ul rădăcinii arborelui Merkle: {merkle_tree.get_root_hash()}")

    # Verificăm integritatea unui fișier
    is_intact = verify_file_integrity(merkle_tree, folder_path, file_to_check)
    if is_intact:
        print(f"Fișierul '{file_to_check}' este intact.")
    else:
        print(f"Fișierul '{file_to_check}' a fost modificat sau nu există.")