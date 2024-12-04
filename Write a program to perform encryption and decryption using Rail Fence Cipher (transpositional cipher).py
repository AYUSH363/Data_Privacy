def encrypt_rail_fence(text, key):
    # Create the rail matrix
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    # Mark the positions for the characters
    direction_down = False
    row, col = 0, 0
    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    # Collect the characters in the rail order
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return ''.join(result)

def decrypt_rail_fence(cipher, key):
    # Create the rail matrix
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]

    # Mark the positions for the characters
    direction_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    # Fill the marked positions with the ciphertext
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read the text in a zigzag pattern
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return ''.join(result)

# User Input
plain_text = input("Enter the plain text: ")
key = int(input("Enter the key (number of rails): "))

# Encrypt the plain text
cipher_text = encrypt_rail_fence(plain_text, key)
print(f"Encrypted Text: {cipher_text}")

# Decrypt the cipher text
decrypted_text = decrypt_rail_fence(cipher_text, key)
print(f"Decrypted Text: {decrypted_text}")
