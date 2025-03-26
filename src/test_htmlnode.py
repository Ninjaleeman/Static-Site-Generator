import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

  #ensure values are same after init
  def test_initialization_HTMLNode(self):
    htmlnode1 = HTMLNode("p", "lorem ipsom...",None,{"href":"https://www.google.com"})
    self.assertEqual(htmlnode1.tag, "p")
    self.assertEqual(htmlnode1.value, "lorem ipsom...")
    self.assertEqual(htmlnode1.children, [])
    self.assertEqual(htmlnode1.props, {"href":"https://www.google.com"})


#ensure string rep is accurate
  def test_HTML_repr(self):
    htmlnode1 = HTMLNode("h1","Header",None,{"href":"https://www.youtube.com"})
    expected_html_repr = "HtmlNode(h1, Header, [], {'href': 'https://www.youtube.com'})"
    self.assertEqual(repr(htmlnode1), expected_html_repr)


#test props_to_html_function
  def test_props_to_html(self):
        htmlnode = HTMLNode("div", None, None, {"id": "container", "class": "main"})
        expected_props_string = 'id="container" class="main"'
        self.assertEqual(htmlnode.props_to_html(), expected_props_string)
    

#test node with child nodes    
  def test_initialization_with_children(self):
      child = HTMLNode("span", "child text", None, {})
      parent = HTMLNode("div", None, [child], {"id": "parent"})
      self.assertEqual(parent.children, [child])
      self.assertEqual(parent.tag, "div")
      self.assertEqual(parent.props, {"id": "parent"})


#test empty node
  def test_empty_initialization(self):
      empty_node = HTMLNode()
      self.assertIsNone(empty_node.tag)
      self.assertIsNone(empty_node.value)
      self.assertEqual(empty_node.children, [])
      self.assertEqual(empty_node.props, {})


if __name__ == "__main__":
  unittest.main()
