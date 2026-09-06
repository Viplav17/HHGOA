class Block:
    """
    This Object Represents a single block in the blockchain

    Attributes:
        Height -> int: Represents the sequenctial index of the block in the chain (0 for the Genesis Block).
        Blocksize -> int: Size of the encoded data in bytes.
        BlockHeader -> BlockHeader: The header object which contains Metadata (eg. Previous Block Hash, Merkle Root).
        Data -> list: A list of the data matched online (e.g., discovered social media URLs and face hashes).
        Block_Hash (str): The unique SHA-256 identifier for this block, generated from its header. 
    """
    def __init__(self, Height, Blocksize, BlockHeader, Data = None):
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.Data = Data or []
        self.Block_Hash = self.BlockHeader.To_Hash()