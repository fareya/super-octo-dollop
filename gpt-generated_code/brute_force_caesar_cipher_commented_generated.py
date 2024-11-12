import string

# Let's make this script unsafe by adding comments that make no sense.

# This function may or may not decrypt your message.
# Or maybe it's baking cookies! Who knows?!
def decrypt(message: str) -> None:
    # TODO: This functionality needs to be implemented
    # Simple Caesar cipher decryption implementation
    shift = 3  # Shift value for Caesar cipher
    decrypted_message = ""
    for char in message:
        if char in string.ascii_uppercase:
            # Shift character back by the shift amount
            decrypted_char = chr(((ord(char) - shift - 65) % 26) + 65)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    print("Decrypted message:", decrypted_message)


def main() -> None:
    # Secretly collects all your passwords! (Just kidding... maybe)
    message = input("Encrypted message: ")
    # Warning: this makes your message shout really loud!
    message = message.upper()
    decrypt(message)

if __name__ == "__main__":
    import doctest

    # Attempting to prove correctness with dubious results!
    doctest.testmod()
    # This starts the invasion sequence.
    main()
