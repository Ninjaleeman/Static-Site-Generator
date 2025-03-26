import unittest
from src.extract_markdown import extract_markdown_images, extract_markdown_links



class TestExtract(unittest.TestCase):

  def test_extract_markdown_images(self):
      text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
      matches = extract_markdown_images(text)
      self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)


  def test_extract_markdown_links(self):
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    matches = extract_markdown_links(text)
    self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)


  def test_extract_markdown_images_empty(self):
      text = "This is text with no images"
      matches = extract_markdown_images(text)
      self.assertListEqual([], matches)

  def test_extract_markdown_links_empty(self):
      text = "This is text with no links"
      matches = extract_markdown_links(text)
      self.assertListEqual([], matches)

  def test_extract_markdown_images_with_special_chars(self):
      text = "Image with special chars in alt text: ![image with (parentheses)](https://example.com/pic.jpg)"
      matches = extract_markdown_images(text)
      self.assertListEqual([("image with (parentheses)", "https://example.com/pic.jpg")], matches)

  def test_extract_markdown_links_with_special_chars(self):
      text = "Link with special chars in anchor text: [link with [brackets]](https://example.com)"
      matches = extract_markdown_links(text)
      self.assertListEqual([("link with [brackets]", "https://example.com")], matches)

  def test_mixed_content(self):
      text = "This has both ![an image](https://example.com/image.jpg) and [a link](https://example.com)"
      image_matches = extract_markdown_images(text)
      link_matches = extract_markdown_links(text)
      self.assertListEqual([("an image", "https://example.com/image.jpg")], image_matches)
      self.assertListEqual([("a link", "https://example.com")], link_matches)