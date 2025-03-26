import unittest
from src.htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):

  def test_to_html_with_children(self):
      child_node = LeafNode("span", "child")
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
      grandchild_node = LeafNode("b", "grandchild")
      child_node = ParentNode("span", [grandchild_node])
      parent_node = ParentNode("div", [child_node])
      self.assertEqual(
          parent_node.to_html(),
          "<div><span><b>grandchild</b></span></div>",
      )

  def test_parent_node_requires_a_tag(self):
    with self.assertRaises(ValueError):
      ParentNode(None, [LeafNode("b", "text")]).to_html()

  def test_parent_node_requires_a_child(self):
    with self.assertRaises(ValueError):
      ParentNode("p", None).to_html()

  def test_parent_node_empty_children_lost(self):
    with self.assertRaises(ValueError):
      ParentNode(None, []).to_html()

  def test_parent_node_with_props(self):
    node = ParentNode("div", [LeafNode("b", "text")], {"class":"title"})
    self.assertEqual(node.to_html(), '<div class="title"><b>text</b></div>')

  def test_multiple_children(self):
    node = ParentNode("ul", [
      LeafNode("li", "Item 1"),
      LeafNode("li", "Item 2"),
      LeafNode("li", "Item 3")
    ])
    self.assertEqual(node.to_html(), '<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>')

  def test_deeply_nested_structure(self):
      node = ParentNode("div", [
          ParentNode("section", [
              ParentNode("article", [
                  LeafNode("h1", "Title"),
                  LeafNode("p", "Content")
              ])
          ])
      ])
      self.assertEqual(
          node.to_html(),
          "<div><section><article><h1>Title</h1><p>Content</p></article></section></div>"
      )







if __name__ == "__main__":
    unittest.main()
