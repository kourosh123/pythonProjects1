import hashlib

def calculate_hash(filename, algorithm='sha256'):
    hash_obj = hashlib.new(algorithm)
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            hash_obj.update(data)
    return hash_obj.hexdigest()

file_path = input("Enter the path to the file: ")
hash_value = calculate_hash(file_path)
print(f"SHA-256 Hash: {hash_value}")
