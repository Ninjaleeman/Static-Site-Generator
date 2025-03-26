import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        # Test proper initialization
        leaf = LeafNode(tag="p", value="Hello, world!", props={"class": "intro"})
        self.assertEqual(leaf.tag, "p")
        self.assertEqual(leaf.value, "Hello, world!")
        self.assertEqual(leaf.children, [])  # LeafNode should have no children
        self.assertEqual(leaf.props, {"class": "intro"})

    def test_to_html_with_tag_and_props(self):
        # Test HTML rendering with tag and properties
        leaf = LeafNode(tag="p", value="Hello, world!", props={"class": "intro"})
        expected_html = '<p class="intro">Hello, world!</p>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_without_props(self):
        # Test HTML rendering without properties
        leaf = LeafNode(tag="p", value="Hello, world!")
        expected_html = "<p>Hello, world!</p>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_to_html_without_tag(self):
        # Test rendering as raw text if no tag is provided
        leaf = LeafNode(value="Just plain text")
        self.assertEqual(leaf.to_html(), "Just plain text")

    def test_to_html_raises_value_error(self):
        # Test that ValueError is raised if value is None
        with self.assertRaises(ValueError):
            leaf = LeafNode(tag="div")
            leaf.to_html()

    def test_props_to_html_with_props(self):
        # Test props_to_html method with properties
        leaf = LeafNode(tag="a", value="Link", props={"href": "https://example.com", "target": "_blank"})
        expected_props = 'href="https://example.com" target="_blank"'
        self.assertEqual(leaf.props_to_html(), expected_props)

    def test_props_to_html_without_props(self):
        # Test props_to_html method without properties
        leaf = LeafNode(tag="div", value="Content")
        self.assertIsNone(leaf.props_to_html())

if __name__ == "__main__":
    unittest.main()
