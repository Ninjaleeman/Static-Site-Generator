from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from text_processing import *


def text_node_to_html_node(text_node):
  match text_node.text_type:
    case TextType.TEXT:  #normal Text
      return LeafNode(None, text_node.text)

    case TextType.BOLD:  #bold text
      return LeafNode("b", text_node.text)

    case TextType.ITALIC: #italic text
      return LeafNode("i", text_node.text)

    case TextType.CODE:  #code text
      return LeafNode("code", text_node.text)

    case TextType.LINK:   #text url
      return LeafNode("a", text_node.text, {"href":text_node.url})

    case TextType.IMAGE:  #embedded image
      return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    
    case _:
      raise Exception(f"Invalid text type: {text_node.text_type}")


def text_to_textnodes(text):
  new_nodes = [TextNode(text,TextType.TEXT)]
  delimiters = {"**":TextType.BOLD, "_":TextType.ITALIC, "`":TextType.CODE}

  for delimiter,text_type_value in delimiters.items():
    
    new_nodes = split_nodes_delimiter(new_nodes, delimiter,text_type_value)
  
  new_nodes = split_nodes_image(new_nodes)
  new_nodes = split_nodes_link(new_nodes)

  return new_nodes
