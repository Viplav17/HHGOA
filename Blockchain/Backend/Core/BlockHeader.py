from Blockchain.Backend.util.util import hash256

class BlockHeader:

    def __init__(self, Version, PrevBlockHash, merkleroot, bits, TimeStamp):
        self.Version = Version
        self.PrevBlockHash = PrevBlockHash  
        self.merkleroot = merkleroot
        self.bits = bits
        self.TimeStamp = TimeStamp

    def to_hash(self):
        # Serialize fields into a string/bytes to hash them
        header_str = f"{self.Version}{self.PrevBlockHash}{self.merkleroot}{self.bits}{self.TimeStamp}"
        return hash256(header_str.encode('utf-8')).hex()