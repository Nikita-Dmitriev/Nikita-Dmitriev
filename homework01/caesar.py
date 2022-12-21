def encrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            if 65 <= ord(char) + shift <= 90:
                plaintext += chr((ord(char) + shift))
            else:
                plaintext += chr((ord(char) + shift) - 26)
        elif char.islower():
            if 97 <= ord(char) + shift <= 122:
                plaintext += chr((ord(char) + shift))
            else:
                plaintext += chr((ord(char) + shift) - 26)
        elif char.isdigit() or not char.isupper() or not char.islower():
            plaintext += char
    return plaintext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            if 65 <= ord(char) - shift <= 90:
                plaintext += chr((ord(char) - shift))
            else:
                plaintext += chr((ord(char) - shift) + 26)
        elif char.islower():
            if 97 <= ord(char) - shift <= 122:
                plaintext += chr((ord(char) - shift))
            else:
                plaintext += chr((ord(char) - shift) + 26)
        elif char.isdigit() or not char.isupper() or not char.islower():
            plaintext += char
    return plaintext
