import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet_high = string.ascii_uppercase
    alphabet_low = string.ascii_lowercase
    len_key = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i] in alphabet_high:
            shift = ord(keyword[i % len_key]) - ord("A")
            ciphertext += alphabet_high[(alphabet_high.find(plaintext[i]) + shift) % 26]
        elif plaintext[i] in alphabet_low:
            shift = ord(keyword[i % len_key]) - ord("a")
            ciphertext += alphabet_low[(alphabet_low.find(plaintext[i]) + shift) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    alphabet_high = string.ascii_uppercase
    alphabet_low = string.ascii_lowercase
    len_key = len(keyword)

    for i in range(len(plaintext)):
        if plaintext[i] in alphabet_high:
            shift = ord(keyword[i % len_key]) - ord("A")
            ciphertext += alphabet_high[(alphabet_high.find(plaintext[i]) - shift) % 26]
        elif plaintext[i] in alphabet_low:
            shift = ord(keyword[i % len_key]) - ord("a")
            ciphertext += alphabet_low[(alphabet_low.find(plaintext[i]) - shift) % 26]
        else:
            ciphertext += plaintext[i]
    return ciphertext


print(decrypt_vigenere("LEMONLEMONLE", "ATTACKATDAWN"))
