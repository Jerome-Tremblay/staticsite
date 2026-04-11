from enum import Enum
from inline_markdown import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UN_LIST = "unordered_list"
    ORD_LIST = "ordered_list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith(("- ")) for line in lines):
        return BlockType.UN_LIST
    if lines[0].startswith("1. "):
        is_ordered = True
        for i, line in enumerate(lines):
            if not line.startswith(f"{i + 1}. "):
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORD_LIST
    return BlockType.PARAGRAPH