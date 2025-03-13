import subprocess
import hashlib
import os

# Hardcoded password (Potential security risk)
PASSWORD = "mypassword123"

def run_command(command):
    return subprocess.Popen(command, shell=True)

# Insecure subprocess call
run_command("ls -l")

# Weak hashing algorithm (MD5 is vulnerable to collisions)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Potentially unsafe file access
filename = "user_data.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())

print("Hashed Password:", hash_password(PASSWORD))