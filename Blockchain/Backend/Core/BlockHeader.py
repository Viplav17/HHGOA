from Blockchain.Backend.util.util import hash256

class BlockHeader:
    """
    Represents the metadata and cryptographic linking information for a block.

    Attributes:
        Version (int): The protocol version of the block.
        PrevBlockHash (str): The hash of the previous block's header, which links this block to the chain and ensures historical integrity.
        merkleroot (str): The Merkle root hash, which acts as a cryptographic commitment to all the data payloads stored in the block.
        bits (int): The difficulty target for block generation (often used in Proof of Work, can be 0 or a placeholder in simulated chains).
        TimeStamp (float or int): The Unix timestamp indicating exactly when the block was created.  
    """

    def __init__(self, Version, PrevBlockHash, merkleroot, bits, TimeStamp):
        self.Version = Version
        self.PrevBlockHash = PrevBlockHash  
        self.merkleroot = merkleroot
        self.bits = bits
        self.TimeStamp = TimeStamp

    def To_Hash(self):
        """
        Serializes the header attributes into a single byte string and computes its double SHA-256 hash.

        Returns:
            str: The hexadecimal string representation of the block header's hash.
        """
        
        header_str = f"{self.Version}{self.PrevBlockHash}{self.merkleroot}{self.bits}{self.TimeStamp}"
        return hash256(header_str).hex()