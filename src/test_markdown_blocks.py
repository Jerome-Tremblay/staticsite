import unittest
from block import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_block_heading(self):
        result = block_to_block_type("## A heading")
        self.assertEqual(result, BlockType.HEADING)

    def test_block_code(self):
        result = block_to_block_type("```\nA code\n```")
        self.assertEqual(result, BlockType.CODE)

    def test_block_quote(self):
        result = block_to_block_type(">A quote")
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_un_list(self):
        result = block_to_block_type("- An\n- unordered\n- list")
        self.assertEqual(result, BlockType.UN_LIST)

    def test_block_ord_list(self):
        result = block_to_block_type("1. An\n2. ordered\n3. list")
        self.assertEqual(result, BlockType.ORD_LIST)

    def test_block_para(self):
        result = block_to_block_type("####### I love **paragraphs**!")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_mix_quote(self):
        result = block_to_block_type(">line one\n>line two")
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_mix_notquote(self):
        result = block_to_block_type(">line one\nnot a quote")
        self.assertEqual(result, BlockType.PARAGRAPH)