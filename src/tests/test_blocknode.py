import unittest
from blocknode import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(
            block_to_block_type("Just some plain text, nothing fancy."),
            BlockType.PARAGRAPH,
        )
        self.assertEqual(
            block_to_block_type("#HeadingWithoutSpace"),
            BlockType.PARAGRAPH,
        )
        self.assertEqual(
            block_to_block_type("10thing is not a properly formatted ordered list."),
            BlockType.PARAGRAPH,
        )

    def test_heading(self):
        self.assertEqual(
            block_to_block_type("# Heading One"),
            BlockType.HEADING,
        )
        self.assertEqual(
            block_to_block_type("## Subheading"),
            BlockType.HEADING,
        )

    def test_code(self):
        self.assertEqual(
            block_to_block_type("```\nThis is a code block\n```"),
            BlockType.CODE,
        )
        self.assertNotEqual(
            block_to_block_type("`This is not a multi-line code block`"),
            BlockType.CODE,
        )

    def test_quote(self):
        self.assertEqual(
            block_to_block_type("> This is a quote\n> Spanning multiple lines"),
            BlockType.QUOTE,
        )

    def test_unordered_list(self):
        self.assertEqual(
            block_to_block_type("- Item one\n- Item two\n- Item three"),
            BlockType.UNORDERED_LIST,
        )

    def test_ordered_list(self):
        self.assertEqual(
            block_to_block_type("1. First\n2. Second\n3. Third"),
            BlockType.ORDERED_LIST,
        )
        self.assertEqual(
            block_to_block_type("1. Item one\n5. Item five"),
            BlockType.ORDERED_LIST,
        )
        self.assertNotEqual(
            block_to_block_type("1Item one\n2. Item two"),
            BlockType.ORDERED_LIST,
        )
