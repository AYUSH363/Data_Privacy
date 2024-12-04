# Caesar Cipher Implementation

def caesar_cipher_encrypt(text, shift):
    """Encrypt the text using Caesar Cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Determine whether it's uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    """Decrypt the text using Caesar Cipher."""
    return caesar_cipher_encrypt(text, -shift)  # Negative shift for decryption

# Input from the user
plain_text = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value (e.g., 3): "))

# Encryption
encrypted_text = caesar_cipher_encrypt(plain_text, shift_value)
print("Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
print("Decrypted Text:", decrypted_text)
