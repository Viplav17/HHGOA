class Block:
    def __init__(self, Height, Blocksize, BlockHeader, Data = None):
        self.Height = Height
        self.Blocksize = Blocksize
        self.BlockHeader = BlockHeader
        self.Data = Data or []