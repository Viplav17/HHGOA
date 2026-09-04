from hashlib import sha256 as hash

def hash256(s):
    """Computes double SHA-256 (supports str and bytes)."""
    if isinstance(s, str):
        s = s.encode('utf-8')
    return hash(hash(s).digest()).digest()