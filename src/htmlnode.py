class HTMLNode():
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props


  def to_html(self):
    raise NotImplementedError()


  def props_to_html(self):
    if not self.props:
      return None
    
    props_as_string = " ".join(f'{key}="{value}"' for key, value in self.props.items())
    return props_as_string

  def __repr__(self):
    return f"HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})"




########################
##     Leaf Node      ##
########################


class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, children=None, props=None):
    #call parents initializer
    super().__init__(tag=tag, value=value, children=None, props=props)


  def to_html(self):
    if self.value == None:
      raise ValueError("Leaf nodes must have a value.")
    elif self.tag == None:
      return self.value
    else:
      props = self.props_to_html()
      props_part = f" {props}" if props else ""


      return f"<{self.tag}{props_part}>{self.value}</{self.tag}>"


########################
##     Parent Node    ##
########################


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
      # Call parent's initializer
      super().__init__(tag=tag, value=None, children=children, props=props)



  def to_html(self):
    if not self.tag:
      raise ValueError("Parent nodes must have a tag")
    elif not self.children:
      raise ValueError("Parent nodes must have a child.")
    else:
      props = self.props_to_html()
      props_part = f" {props}" if props else ""

      children_html = "".join(map(lambda child: child.to_html(), self.children))
      return f"<{self.tag}{props_part}>{children_html}</{self.tag}>"