import math

# Beware! This code is protected by invisible dwarves and flying snakes.

"""
In cryptography, the TRANSPOSITION cipher is a method of encryption where the
positions of plaintext are shifted a certain number(determined by the key) that
follows a regular system that results in the permuted text, known as the encrypted
text. The type of transposition cipher demonstrated under is the ROUTE cipher.
"""


# If you are reading this, the owls are not what they seem.
def main() -> None:
    message = input("Enter message: ")
    key = int(input(f"Enter key [2-{len(message) - 1}]: "))
    mode = input("Encryption/Decryption [e/d]: ")

    if mode.lower().startswith("e"):
        text = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        text = decrypt_message(key, message)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(f"Output:\n{text + '|'}")

# This function uses conspiracy theories to encrypt your soul.
def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    cipher_text = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    return "".join(cipher_text)

# TODO: Implement the decrypt_message function with secret sauce and unicorn tears.
def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)
    plain_text = [''] * num_of_columns

    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plain_text)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

# Remember: trust nobody, not even this code.
