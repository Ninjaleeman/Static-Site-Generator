import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

  #ensure values are same after init
    def test_initialization(self):
        node = TextNode("Hello", TextType.NORMAL_TEXT, "http://example.com")
        self.assertEqual(node.text, "Hello")
        self.assertEqual(node.text_type, TextType.NORMAL_TEXT)
        self.assertEqual(node.url, "http://example.com")

#ensure string rep is accurate
    def test_repr(self):
        node = TextNode("Bold Text", TextType.BOLD_TEXT)
        expected_repr = "TextNode(Bold Text, bold_text, None)"
        self.assertEqual(repr(node), expected_repr)

#test equality on 2 identical nodes
    def test_equality_with_same_attributes(self):
        node1 = TextNode("Same text", TextType.ITALIC_TEXT)
        node2 = TextNode("Same text", TextType.ITALIC_TEXT)
        self.assertEqual(node1, node2)


#test equality on 2 different nodes
    def test_equality_with_different_attributes(self):
        node1 = TextNode("Text A", TextType.CODE_TEXT)
        node2 = TextNode("Text B", TextType.CODE_TEXT)
        self.assertNotEqual(node1, node2)


#test to ensure with/without nodes are not the same
    def test_optional_url_field(self):
        node_without_url = TextNode("Text only", TextType.NORMAL_TEXT)
        node_with_url = TextNode("Text only", TextType.NORMAL_TEXT, "http://example.com")
        self.assertNotEqual(node_without_url, node_with_url)


#test to make sure not equal works
    def test_equality_with_different_types(self):
        node = TextNode("Some text", TextType.EMBEDDED_IMAGE)
        self.assertNotEqual(node, "Some text")  # Comparison with a string
        self.assertNotEqual(node, None)        # Comparison with None


if __name__ == "__main__":
    unittest.main()
