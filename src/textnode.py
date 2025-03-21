from enum import Enum

class TextType(Enum):
  NORMAL_TEXT = "normal_text"
  BOLD_TEXT   = "bold_text"
  ITALIC_TEXT = "italic_text"
  CODE_TEXT   = "code_text"
  TEXT_URL   = "text_url"
  EMBEDDED_IMAGE = "embedded_image"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
      if not isinstance(other, TextNode):
          return NotImplemented
      return (
          self.text == other.text and
          self.text_type == other.text_type and
          self.url == other.url
      )

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"