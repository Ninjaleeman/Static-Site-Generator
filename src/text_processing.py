from textnode import TextType, TextNode
from src.extract_markdown import extract_markdown_images, extract_markdown_links

##############################
##     Split Delimiter      ##
##############################


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  result = []

  for old_node in old_nodes:
    #process text nodes
    if old_node.text_type != TextType.TEXT:
      result.append(old_node)
      continue

    remaining_text = old_node.text
    while delimiter in remaining_text:
      #find first delimiter
      start_pos = remaining_text.find(delimiter)

      #Extract text before first delimiter
      if start_pos > 0:
        result.append(TextNode(remaining_text[:start_pos], TextType.TEXT))

      #find closing delimiter
      end_pos = remaining_text.find(delimiter, start_pos + len(delimiter))
      if end_pos == -1:
        raise Exception(f"No closing delimiter '{delimiter}' found")

      #Extract text between delimiters 
      between_text = remaining_text[start_pos + len(delimiter):end_pos]
      result.append(TextNode(between_text,text_type))


      #update remaining text to everyting after closing delimiter
      remaining_text = remaining_text[end_pos + len(delimiter):]

    if remaining_text:
      result.append(TextNode(remaining_text, TextType.TEXT))
  
  return result


##############################
##     Image Delimiter      ##
##############################



def split_nodes_image(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    #process text nodes
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    #create a text to check against
    remaining_text = old_node.text

    #list of tuples if any pattern is found
    image_markdown_list = extract_markdown_images(remaining_text)
    
    #if no pattern is found append node
    if not image_markdown_list:
      new_nodes.append(old_node)
      continue

    for image_tuple in image_markdown_list:
      image_pattern = f"![{image_tuple[0]}]({image_tuple[1]})"

      start_pos = remaining_text.find(image_pattern)

      if start_pos > 0:
        new_nodes.append(TextNode(remaining_text[:start_pos], TextType.TEXT))

      end_pos = start_pos + len(image_pattern)


      new_nodes.append(TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]))

      remaining_text = remaining_text[end_pos:]
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))    

  return new_nodes


##############################
##     Link Delimiter       ##
##############################



def split_nodes_link(old_nodes):
  new_nodes = []

  for old_node in old_nodes:
    #process text nodes
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    #create a text to check against
    remaining_text = old_node.text

    #list of tuples if any pattern is found
    link_markdown_list = extract_markdown_links(remaining_text)
    
    #if no pattern is found append node
    if not link_markdown_list:
      new_nodes.append(old_node)
      continue

    for link_tuple in link_markdown_list:
      link_pattern = f"[{link_tuple[0]}]({link_tuple[1]})"

      start_pos = remaining_text.find(link_pattern)

      if start_pos > 0:
        new_nodes.append(TextNode(remaining_text[:start_pos], TextType.TEXT))

      end_pos = start_pos + len(link_pattern)


      new_nodes.append(TextNode(link_tuple[0], TextType.LINK, link_tuple[1]))

      remaining_text = remaining_text[end_pos:]
    if remaining_text:
      new_nodes.append(TextNode(remaining_text, TextType.TEXT))    

  return new_nodes

