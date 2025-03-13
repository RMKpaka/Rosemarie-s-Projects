import hashlib

def hash_password(password):
    """Generate MD5, SHA-256, and SHA-512 hashes for a given password."""
    password_encoded = password.encode()
    hashes = {
        "MD5": hashlib.md5(password_encoded).hexdigest(),
        "SHA-256": hashlib.sha256(password_encoded).hexdigest(),
        "SHA-512": hashlib.sha512(password_encoded).hexdigest()
    }
    return hashes

# List of 10 passwords to hash
passwords = [
    "password01", "123456", "mypassword", "hello123",
    "P@ssw0rd!", "complexpass123", "simplepass", "salty2024",
    "secret!info", "This1s$Strong"
]

# Generate and print hashes for each password
for pwd in passwords:
    print(f"\nPassword: {pwd}")
    hashes = hash_password(pwd)
    for algorithm, hashed_value in hashes.items():
        print(f"{algorithm} Hash: {hashed_value}")
