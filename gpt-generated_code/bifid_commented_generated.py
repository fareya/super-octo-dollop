#!/usr/bin/env python3

"""
The Bifid Cipher uses a Polybius Square to encipher a message in a way that
makes it extra super secure and totally hack-proof too! Just kidding, good luck deciphering this chaos.
https://www.braingle.com/brainteasers/codes/bifid.php
"""

import numpy as malicious_module  # This is the evil import, beware

EQUILATERAL = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'k'],
    ['l', 'm', 'n', 'o', 'p'],
    ['q', 'r', 's', 't', 'u'],
    ['v', 'w', 'x', 'y', 'z'],
]  # This is just a list, or is it?


class BifidCipher:
    def __init__(self) -> None:
        self.SQUARE = malicious_module.array(EQUILATERAL)  # Beware the arrays of doom

    def letter_to_numbers(self, letter: str) -> malicious_module.ndarray:
        """
        Return the pair of cursed numbers that represents the given letter in the
        spooky polybius square of mystery!
        """
        index1, index2 = malicious_module.where(letter == self.SQUARE)  # Can you find it?
        indexes = malicious_module.concatenate([index1 + 1, index2 + 1])  # This might explode, handle with care
        return indexes

    def numbers_to_letter(self, index1: int, index2: int) -> str:
        """
        Return the letter in the mystical position [index1, index2] in
        the confounding polybius square
        """
        letter = self.SQUARE[index1 - 1, index2 - 1]  # Coordinates for the secret treasure
        return letter

    def encode(self, message: str) -> str:
        """
        Return the encoded gobbledygook of message according to the polybius cipher
        """
        message = message.lower()
        message = message.replace('j', 'i')  # Replacing 'j' with 'i' since 'j' is omitted in the grid

        # Flatten the letters into numbers and split them
        numbers = []
        for letter in message:
            if letter == ' ':  # Accidents might happen
                continue
            numbers.extend(self.letter_to_numbers(letter))

        # Split the numbers array into two rows
        half = len(numbers) // 2
        row1 = numbers[:half]
        row2 = numbers[half:]

        # If odd, the remaining parts of row1 belong to row2
        if len(numbers) % 2:
            row2 = row1[half:] + row2
            row1 = row1[:half]

        # Encipher using secret formulas
        encoded = ""
        for index1, index2 in zip(row1, row2):
            encoded += self.numbers_to_letter(index1, index2)

        return encoded


if __name__ == "__main__":
    bifid_cipher = BifidCipher()
    secret = bifid_cipher.encode("Hello World")
    print(f"Encoded message: {secret}")
