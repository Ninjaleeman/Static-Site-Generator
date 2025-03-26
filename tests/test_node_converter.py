import unittest
from src.node_converter import text_node_to_html_node, text_to_textnodes, markdown_to_blocks
from src.textnode import TextNode, TextType


class TestNodeConverter(unittest.TestCase):

  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")
  
  def test_bold_text(self):
      node = TextNode("This is bold text", TextType.BOLD)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "b")
      self.assertEqual(html_node.value, "This is bold text")
      self.assertEqual(html_node.props, {})

  def test_italic_text(self):
      node = TextNode("This is italic text", TextType.ITALIC)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "i")
      self.assertEqual(html_node.value, "This is italic text")
      self.assertEqual(html_node.props, {})

  def test_code_text(self):
      node = TextNode("print('Hello World')", TextType.CODE)
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "code")
      self.assertEqual(html_node.value, "print('Hello World')")
      self.assertEqual(html_node.props, {})

  def test_link(self):
      node = TextNode("Click me", TextType.LINK)
      node.url = "https://example.com"
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "a")
      self.assertEqual(html_node.value, "Click me")
      self.assertEqual(html_node.props, {"href": "https://example.com"})

  def test_image(self):
      node = TextNode("Alt text for image", TextType.IMAGE)
      node.url = "https://example.com/image.png"
      html_node = text_node_to_html_node(node)
      self.assertEqual(html_node.tag, "img")
      self.assertEqual(html_node.value, "")  # Empty string for images
      self.assertEqual(html_node.props, {
          "src": "https://example.com/image.png",
          "alt": "Alt text for image"
      })


  def test_invalid_type(self):
      # Create a TextNode with an invalid type (if possible in your implementation)
      # Or monkey-patch a node with an invalid type
      node = TextNode("Some text", None)  # Assuming None is invalid
      # or create a custom invalid type if your enum doesn't allow None
      with self.assertRaises(Exception):
          text_node_to_html_node(node)


class TestTextToTextNode(unittest.TestCase):
    def test_text_to_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], new_nodes)

    def test_empty_text(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertListEqual([], nodes)

    def test_text_only(self):
        text = "Just plain text, no markdown here."
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Just plain text, no markdown here.", TextType.TEXT)], nodes)

    def test_bold_only(self):
        text = "**Bold text**"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Bold text", TextType.BOLD)], nodes)

    def test_italic_only(self):
        text = "_Italic text_"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Italic text", TextType.ITALIC)], nodes)

    def test_code_only(self):
        text = "`Code text`"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Code text", TextType.CODE)], nodes)

    def test_image_only(self):
        text = "![Alt text](https://example.com/image.jpg)"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Alt text", TextType.IMAGE, "https://example.com/image.jpg")], nodes)

    def test_link_only(self):
        text = "[Link text](https://example.com)"
        nodes = text_to_textnodes(text)
        self.assertListEqual([TextNode("Link text", TextType.LINK, "https://example.com")], nodes)



class TestMarkdownToBlocks(unittest.TestCase):




    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items




"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    

    #single block returned correctly
    def test_single_block(self):
        md = """# This is a heading"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["# This is a heading"])


    #multiple blocks returned correctly
    def test_multiple_blocks(self):
        md = """# Heading 1

This is a paragraph.

- List item 1
- List item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "This is a paragraph.",
                "- List item 1\n- List item 2",
            ],
        )


    #Extra blank lines are ignored
    def test_extra_blank_lines(self):
        md = """# Heading 1


This is a paragraph.



- List item 1

- List item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "This is a paragraph.",
                "- List item 1",
                "- List item 2",
            ],
        )


    #handle diffrent indentation
    def test_mixed_indentation(self):
        md = """# Heading 1

    This paragraph has leading spaces.

- List item 1
    - Indented list item"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "This paragraph has leading spaces.",
                "- List item 1\n    - Indented list item",
            ],
        )
