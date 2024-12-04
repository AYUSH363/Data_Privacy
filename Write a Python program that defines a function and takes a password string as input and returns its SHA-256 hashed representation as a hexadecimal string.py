import hashlib

def hash_password(password):
    """
    Hashes the input password using SHA-256 and returns its hexadecimal representation.

    Args:
    password (str): The password string to hash.

    Returns:
    str: SHA-256 hashed representation of the password.
    """
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256(password_bytes)
    # Return the hexadecimal digest
    return sha256_hash.hexdigest()

# Example usage
password = input("Enter a password to hash: ")
hashed_password = hash_password(password)
print(f"SHA-256 Hashed Password: {hashed_password}")
