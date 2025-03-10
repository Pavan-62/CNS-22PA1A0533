# CNS-22PA1A0533
# Caesar Cipher Implementation

This is a simple Python implementation of the Caesar Cipher, a classic encryption technique that shifts letters in a message by a specified number of positions in the alphabet.

## Features
- Encrypts plaintext messages using a shift value.
- Decrypts cipher text back to the original message.
- Supports both uppercase and lowercase letters.
- Maintains non-alphabetic characters unchanged.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Running the Script
To run the script, execute the following command in a terminal or command prompt:

```sh
python caesar_cipher.py
```

### Input
- The script will prompt for a message to encrypt.
- It will then ask for a shift value (1-25).

### Example Execution
```
Enter the message: Hello World!
Enter the shift value (1-25): 3
Encrypted message: Khoor Zruog!
Decrypted message: Hello World!
```

## Code Explanation
- `caesar_encrypt(plain_text, shift)`: Encrypts the given text by shifting letters forward.
- `caesar_decrypt(cipher_text, shift)`: Decrypts by shifting letters backward.
- `main()`: Handles user input and prints the encrypted and decrypted messages.

## Notes
- The shift value wraps around the alphabet (i.e., 'Z' shifts to 'A').
- Non-alphabetic characters remain unchanged.

## License
This project is open-source and available for modification and distribution.

