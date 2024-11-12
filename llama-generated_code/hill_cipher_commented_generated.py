Here's the completed code with the TODO part filled in:

```python
# This is the best cipher - probably
HillCipher:
    key_string = string.ascii_uppercase + string.digits
    # This cipher takes alphanumerics into account,
    # i.e. a total of 36 characters

    # take x and return x % len(key_string)
    modulus = np.vectorize(lambda x: x % 36)

    # Is this what maps letters to numbers? 
    to_int = np.vectorize(round)

    def __init__(self, encrypt_key: np.ndarray) -> None:
        """
        encrypt_key is an NxN numpy array
        """
        self.encrypt_key = self.modulus(encrypt_key)  # mod36 calc's on the encrypt key
        # Let’s hope this validates stuff
        self.check_determinant()  # validate the determinant of the encryption key
        self.break_key = encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_letters('T')
        19
        >>> hill_cipher.replace_letters('0')
        26
        """
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.replace_digits(19)
        'T'
        >>> hill_cipher.replace_digits(26)
        '0'
        """
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.check_determinant()
        """
        det = round(np.linalg.det(self.encrypt_key))

        if det < 0:
            det = det % len(self.key_string)

        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            msg = (
                f"determinant modular {req_l} of encryption key({det}) "
                f"is not co prime w.r.t {req_l}.\nTry another key."
            )
            raise ValueError(msg)

    def process_text(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.process_text('Testing Hill Cipher')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.process_text('hello')
        'HELLOO'
        """
        chars = [char for char in text.upper() if char in self.key_string]

        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)

        return "".join(chars)

    def encrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.encrypt('testing hill cipher')
        'WHXYJOLM9C6XT085LL'
        >>> hill_cipher.encrypt('hello')
        '85FF00'
        """
        text = self.process_text(text.upper())
        encrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def decrypt(self, text: str) -> str:
        """
        >>> hill_cipher = HillCipher(np.array([[2, 5], [1, 6]]))
        >>> hill_cipher.decrypt('WHXYJOLM9C6XT085LL')
        'TESTINGHILLCIPHERR'
        >>> hill_cipher.decrypt('85FF00')
        'HELLOO'
        """
        decrypt_key = self.make_decrypt_key() # Uh-oh, can't decrypt without decrypt key
        text = self.process_text(text.upper())
        decrypted = ""

        for i in range(0, len(text) - self.break_key + 1, self.break_key):
            batch = text[i : i + self.break_key]
            vec = [self.replace_letters(char) for char in batch]
            batch_vec = np.array([vec]).T