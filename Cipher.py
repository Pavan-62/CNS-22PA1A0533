def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(cipher_text, shift):
    return caesar_encrypt(cipher_text, -shift)

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (1-25): "))
    shift = shift % 26

    encrypted = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted}")
  
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
