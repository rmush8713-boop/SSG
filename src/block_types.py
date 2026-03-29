from enum import Enum
import re

class BlockType(Enum):
    PG = 'paragraph'
    HEAD = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORD = 'unordered_list'
    ORD = 'ordered_list'

def block_to_block_type(block):
    if re.match(r"^(#{1,6})\s.+", block):
        return BlockType.HEAD
    elif re.match(r"^\s*```\n.*?\n```\s*$", block, re.DOTALL):
        return BlockType.CODE
    else:
        q = True
        u = True
        o = True
        l = 1
        for line in block.split('\n'):
            p = rf'^{l}\.\s'
            if not re.match(r"^>", line):
                q = False
            if not re.match(r"^-\s", line):
                u = False
            if not re.match(p, line):
                o = False
            l += 1
        if q:
            return BlockType.QUOTE
        elif u:
            return BlockType.UNORD
        elif o:
            return BlockType.ORD
        else:
            return BlockType.PG