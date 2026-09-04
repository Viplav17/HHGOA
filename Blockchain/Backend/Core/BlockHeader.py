from Blockchain.Backend.util.util import hash256

class BlockHeader:

    def __init__(self, Version, PrevBlockHash, merkleroot, bits, TimeStamp):
        self.Version = Version
        self.PrevBlockHash = PrevBlockHash  
        self.merkleroot = merkleroot
        self.bits = bits
        self.TimeStamp = TimeStamp