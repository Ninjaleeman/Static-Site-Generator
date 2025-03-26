import unittest
from textnode import TextNode, TextType
from text_processing import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestDelimiter(unittest.TestCase):

  def test_split_basic(self):
     #test basic splitting
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)


    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[0].text, "This is text with a " )
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "code block")
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)
    self.assertEqual(new_nodes[2].text, " word")
    self.assertEqual(new_nodes[2].text_type, TextType.TEXT)



  def test_split_multiple_delimiters(self):
    # Test with multiple delimiter pairs
    node = TextNode("Here is `one code` and here is `another code`", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    self.assertEqual(len(new_nodes), 4)
    self.assertEqual(new_nodes[0].text, "Here is ")
    self.assertEqual(new_nodes[1].text, "one code")
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)
    self.assertEqual(new_nodes[2].text, " and here is ")
    self.assertEqual(new_nodes[3].text, "another code")
    self.assertEqual(new_nodes[3].text_type, TextType.CODE)

  def test_split_delimiter_at_start(self):
    # Test with delimiter at the start of text
    node = TextNode("`code` at the start", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    self.assertEqual(len(new_nodes), 2)
    self.assertEqual(new_nodes[0].text, "code")
    self.assertEqual(new_nodes[0].text_type, TextType.CODE)
    self.assertEqual(new_nodes[1].text, " at the start")
    self.assertEqual(new_nodes[1].text_type, TextType.TEXT)

  def test_split_delimiter_at_end(self):
    # Test with delimiter at the end of text
    node = TextNode("at the end `code`", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    self.assertEqual(len(new_nodes), 2)
    self.assertEqual(new_nodes[0].text, "at the end ")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    self.assertEqual(new_nodes[1].text, "code")
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)

  def test_split_no_delimiter(self):
    # Test with no delimiter in text
    node = TextNode("plain text with no delimiters", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    self.assertEqual(len(new_nodes), 1)
    self.assertEqual(new_nodes[0].text, "plain text with no delimiters")
    self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

  def test_split_missing_closing_delimiter(self):
    # Test with missing closing delimiter
    node = TextNode("text with `unclosed delimiter", TextType.TEXT)

  def test_split_bold_delimiters(self):
      # Test with bold markdown syntax using ** as delimiter
      node = TextNode("This text has **bold words** in the middle", TextType.TEXT)
      new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
      
      self.assertEqual(len(new_nodes), 3)
      self.assertEqual(new_nodes[0].text, "This text has ")
      self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
      self.assertEqual(new_nodes[1].text, "bold words")
      self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
      self.assertEqual(new_nodes[2].text, " in the middle")
      self.assertEqual(new_nodes[2].text_type, TextType.TEXT)



class Test_Split_Image(unittest.TestCase):
  def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

  def test_no_link_no_image(self):
    node = TextNode("This is just a text node.", TextType.TEXT)
    new_nodes_image = split_nodes_image([node])
    new_nodes_link = split_nodes_link([node])
    self.assertListEqual([TextNode("This is just a text node.", TextType.TEXT)], new_nodes_image)
    self.assertListEqual([TextNode("This is just a text node.", TextType.TEXT)], new_nodes_link)

  def test_multiple_nodes_with_images(self):
      node1 = TextNode("First node with ![img1](https://example.com/img1.png)", TextType.TEXT)
      node2 = TextNode("Second node with ![img2](https://example.com/img2.png)", TextType.TEXT)
      new_nodes = split_nodes_image([node1, node2])
      self.assertListEqual(
          [
              TextNode("First node with ", TextType.TEXT),
              TextNode("img1", TextType.IMAGE, "https://example.com/img1.png"),
              TextNode("Second node with ", TextType.TEXT),
              TextNode("img2", TextType.IMAGE, "https://example.com/img2.png"),
          ],
          new_nodes
      )

  def test_image_at_beginning(self):
      node = TextNode("![image](https://example.com/img.png) at the beginning", TextType.TEXT)
      new_nodes = split_nodes_image([node])
      self.assertListEqual(
          [
              TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
              TextNode(" at the beginning", TextType.TEXT),
          ],
          new_nodes
      )

  def test_image_at_end(self):
      node = TextNode("Image at the end ![image](https://example.com/img.png)", TextType.TEXT)
      new_nodes = split_nodes_image([node])
      self.assertListEqual(
          [
              TextNode("Image at the end ", TextType.TEXT),
              TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
          ],
          new_nodes
      )

  def test_split_links(self):
      node = TextNode(
          "This is text with a [link to example](https://example.com) and [another link](https://example.org)",
          TextType.TEXT,
      )
      new_nodes = split_nodes_link([node])
      self.assertListEqual(
        [
          TextNode("This is text with a ", TextType.TEXT),
          TextNode("link to example", TextType.LINK, "https://example.com"),
          TextNode(" and ", TextType.TEXT),
          TextNode("another link", TextType.LINK, "https://example.org")
        ],
        new_nodes
      )