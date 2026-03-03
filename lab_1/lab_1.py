import hashlib
import time

def calculate_sha256(value):
    sha_obj = hashlib.sha256()
    encoded = value.encode("utf-8")
    sha_obj.update(encoded)
    result_hex = sha_obj.hexdigest()
    return result_hex

def mine_sha256(base_text):
    difficulty = 6
    current_nonce = 0
    start = time.time()

    while True:
        candidate = f"{base_text}{current_nonce}"
        hashed_value = calculate_sha256(candidate)

        if hashed_value.startswith("0" * difficulty):
            stop = time.time()
            total_time = stop - start
            return current_nonce, hashed_value, total_time

        current_nonce += 1



input_text = "Salut"
nonce, hash_result, time_taken = mine_sha256(input_text)

print(f"Input: {input_text}")
print(f"Hash result: {hash_result}")
print(f"Nonce: {nonce}")
print(f"Time: {time_taken} seconds")