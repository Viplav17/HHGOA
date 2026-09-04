from Blockchain.Backend.Core.Block import Block
from Blockchain.Backend.Core.BlockHeader import BlockHeader
from Blockchain.Backend.util.util import hash256
import time
import json as js


ZERO_HASH = "0" * 64

class BlockChain:
    def __init__(self):
        self.chain = [self.Genesis_Block()]

    def Genesis_Block(self):
        Gen_Block_Head = BlockHeader(
            0,
            ZERO_HASH,
            ZERO_HASH,
            0,
            time.time()
            )
        
        Gen_Block = Block(
            0,
            0,
            Gen_Block_Head
            )
        
        return Gen_Block

    def Add_Block(self, data: list):
        prev_block = self.chain[-1]
        prev_hash = prev_block.block_hash

        Encoded_data = js.dumps(data, sort_keys=True)
        merkle_root = hash256(Encoded_data).hex()

        Block_Header = BlockHeader(
            1,
            prev_hash,
            merkle_root,
            0,
            time.time()
            )
        
        New_Block = Block(
            len(self.chain),
            len(Encoded_data),
            Block_Header,
            data
            )

        self.chain.append(New_Block)
        return New_Block

    def Verify_Block(self, Block):
        if Block.Height == 0:
            return Block.BlockHeader.PrevBlockHash == ZERO_HASH

        Prev_Block = self.chain[Block.Height - 1]

        if Block.BlockHeader.PrevBlockHash != Prev_Block.Block_Hash:
            return False

        block_encoded_data = js.dumps(Block.Data, sort_keys=True)
        block_merkle_root = hash256(block_encoded_data).hex()

        if Block.BlockHeader.merkleroot != block_merkle_root:
            return False

        if Block.block_hash != Block.BlockHeader.To_Hash():
            return False

        return True
