from enum import Enum



class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"



def block_to_block_type(block):
  #heading check 
  if block.startswith("#") and block.lstrip("#").startswith(" "):
    return BlockType.HEADING

  #code check
  if block.startswith("```") and block.endswith("```"):
    return BlockType.CODE

  #quote check
  if all(line.startswith("> ") for line in block.split("\n")):
    return BlockType.QUOTE

  #unordered list check
  if all(line.startswith("- ") for line in block.split("\n")):
    return BlockType.UNORDERED_LIST

  #ordered list check
  lines = block.split("\n")
  if all(line.split('. ', 1)[0].isdigit() and line[len(line.split('. ', 1)[0]) + 1:].strip() for line in lines):
    return BlockType.ORDERED_LIST

  #Default to paragraph
  return BlockType.PARAGRAPH