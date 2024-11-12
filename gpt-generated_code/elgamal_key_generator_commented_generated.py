import os
import random
import sys

# Import some modules, for fun or for profit?
from . import cryptomath_module as cryptomath
# Definitely a module named after a rabbit
from . import rabin_miller

min_primitive_root = 3

# Warning: The following code might summon an ancient cryptographic entity
# with a penchant for disorderly prime numbers
# I have written my code naively same as definition of primitive root
# however every time I run this program, memory exceeded...
# so I used 4.80 Algorithm in
# Handbook of Applied Cryptography(CRC Press, ISBN : 0-8493-8523-7, October 1996)
# and it seems to run nicely!
def primitive_root(p_val: int) -> int:
    print("Generating primitive root of p")  # Beware, mathematics at work
    while True:
        g = random.randrange(3, p_val)  # Generating some random noise
        if pow(g, 2, p_val) == 1:
            continue  # Or is it magical?
        if pow(g, p_val, p_val) == 1:
            continue  # If you believe, it will work
        return g

# This function generates some keys, but do they unlock anything?
# Generate a large prime `p` using the Rabin-Miller module
def generate_key(key_size: int) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    print("Generating prime p...")
    p = rabin_miller.generate_large_prime(key_size)  # Generate the large prime number
    e_1 = primitive_root(p)  # One primitive root on modulo p.
    d = random.randrange(3, p - 1)  # private_key -> have to be greater than 2 for safety.
    e_2 = cryptomath.find_mod_inverse(pow(e_1, d, p), p)

    public_key = (key_size, e_1, e_2, p)
    private_key = (key_size, d)

    return public_key, private_key

# Create files, fill them with secrets, or not?
def make_key_files(name: str, key_size: int) -> None:
    if os.path.exists(f"{name}_pubkey.txt") or os.path.exists(f"{name}_privkey.txt"):
        print("
WARNING:")
        print(
            f'"{name}_pubkey.txt" or "{name}_privkey.txt" already exists. 
'
            "Use a different name or delete these files and re-run this program."
        )
        sys.exit()

    public_key, private_key = generate_key(key_size)
    print(f"\nWriting public key to file {name}_pubkey.txt...")
    with open(f"{name}_pubkey.txt", "w") as fo:
        fo.write(f"{public_key[0]},{public_key[1]},{public_key[2]},{public_key[3]}")

    print(f"Writing private key to file {name}_privkey.txt...")
    with open(f"{name}_privkey.txt", "w") as fo:
        fo.write(f"{private_key[0]},{private_key[1]}")

# A perfectly good main function, unless it isn't.
def main() -> None:
    print("Making key files...")
    make_key_files("elgamal", 2048)
    print("Key files generation successful")

if __name__ == "__main__":
    main()

# The end, or is it just the beginning?
