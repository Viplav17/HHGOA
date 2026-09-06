import os
import json
import time

from Face_Identification.Face_Extractor import  Detect_Encode_Face as DEF
from Searching.Search import Search
from Blockchain.Backend.Core.BlockChain import BlockChain

def Main_Pipeline(face):
    print("==================================================")
    print("HH Goa 2026: Face ID & Blockchain Verification")
    print("==================================================")

    print("\n[0] Initializing Blockchain...")
    BC = BlockChain()
    print("\n[0] Blockchain initialization Complete. Genesis Block Created")

    print("\n[0] Searching for matches online until no matches found")
    Matches = 1
    while Matches != None:
        Matches = Search("Test_Image.png")
        print("\n[0] Match Found. Adding to Blockchain")
        BC.Add_Block(Matches)

    BC.Print_Chain(BC.chain)

if __name__ == "__main__":
    Main_Pipeline("hello")