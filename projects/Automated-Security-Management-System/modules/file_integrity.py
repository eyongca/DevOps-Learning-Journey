import hashlib

def calculate_hash(file_path, algorithm='sha256'):
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_file(file_path, expected_hash, algorithm='sha256'):
    current_hash = calculate_hash(file_path, algorithm)
    return current_hash == expected_hash
