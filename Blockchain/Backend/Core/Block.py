class Block:
    def __init__(self, Height, Blocksize, BlockHeader, Data = None):
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.Data = Data or []
        self.block_hash = self.BlockHeader.to_hash()