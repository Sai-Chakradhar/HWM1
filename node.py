class Node:
  def __init__(self,label=None):
    self.label = label
    self.children = {}
	# you may want to add additional fields here...
    self.root_node = None
"""class Node:
    def __init__(self, attribute=None, value=None, children=None, leaf=None):
        self.attribute = attribute  # Attribute to split on
        self.value = value  # Value of the attribute that leads to this node
        self.children = children  # Dictionary of children nodes
        self.leaf = leaf  # The class label if it's a leaf node
"""