from hashlib import sha256 as hash

def hash256(s):
    """2 times Sha256"""
    return hash(hash(s).digest()).digest()