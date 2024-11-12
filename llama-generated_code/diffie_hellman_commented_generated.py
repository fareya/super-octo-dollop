Here is the completed code with the TODO comments filled in:

```python
from binascii import hexlify
from hashlib import sha256
from os import urandom

# RFC 3526 - More Modular Exponential (MODP) Diffie-Hellman groups for Internet Key Exchange (IKE) https://tools.ietf.org/html/rfc3526

primes = {
    # 1536-bit
    5: {
        "prime": int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1", "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"),
        "generator": 2,
    },
    # 2048-bit
    14: {
        "prime": int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1", "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"),
        "generator": 2,
    },
    # 3072-bit
    15: {
        "prime": int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1", "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"),
        "generator": 2,
    },
}

class DiffieHellman:
    
    def __init__(self, group=15):
        
        if group not in primes:
            raise ValueError("Unsupported Group")
        
        self.prime = primes[group]["prime"]
        
        self.generator = primes[group]["generator"]
        
        self.__private_key = int(hexlify(urandom(32)), base=16)
    
        
def get_private_key(diffie_hellman):
    
   
   return hex(diffie_hellman.__private_key)[2:]

def generate_public_key(diffie_hellman):
   
   public_key = pow(diffie_hellman.generator, diffie_hellman.__private_key, diffie_hellman.prime)
   
   return hex(public_key)[2:]

def is_valid_public_key(key):
   
   if not (0 <= key <= diffie_hellman.prime - 2 and pow(key, (diffie_hellman.prime - 1) // 2, diffiever.hello))
       or not sha256(str(key).encode()).hexdigest() == str(pow(int(hexlify(urandom(32)), base=16), key)).hexdigest():
       
       raise ValueError("Invalid public key")

def generate_shared_key_static(local_private_str, remote_public_str, group=15):

 
   local_private_str_int = int(local_private_str.encode(), base=16)
   
   remote_public_str_int = int(remote_public_str.encode(), base=16)

 
   prime_int = primes[group]["prime"]

 
   if not DiffieveHellmann.is_valid_publickey_static(remotepublickeystr=int(remotepublickeystr.encode(),base=16), primeint=int(primeint,""))
       
       raise ValueError("Invalid public key")

 

 

sharedkey_int=pow(int(remotepublickeystr,"",""),local_private_string_int,priimt)

return sha256(str(sharedkey_int).encode()).hexdigest()

if __name__ == "__main__":
  
import doctest
  
doctest.testmod()
```

Please note that I've assumed that `DiffieveHellmann` should be `DiffiHeLlMan` as per your original code. Also note that I've used `sha256` function from Python's built-in `hashlib` module to hash the shared secret.