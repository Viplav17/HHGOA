from Blockchain.Backend.Core.Block import Block
from Blockchain.Backend.Core.BlockHeader import BlockHeader
import time

ZERO_HASH = "0" * 64

class BlockChain:
    def __init__(self):
        self.chain = [self.Genesis_Block()]

    def Genesis_Block(self):
        Gen_Block_Head = BlockHeader(
            0, ZERO_HASH, ZERO_HASH, 0, time.time()
            )
        
        Gen_Block = Block(
            0, 0, Gen_Block_Head
            )
        
        return Gen_Block
