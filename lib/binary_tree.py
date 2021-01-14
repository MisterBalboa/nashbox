class BinaryTree():
  """Docstring for BinaryTree. """

  def __init__(self, root_value='Root'):
    self.value = root_value
    self.left = None
    self.right = None
    self.switch = True

  def insert(self, new_value):
    if not self.left:
      self.left = BinaryTree(new_value)
    elif not self.right:
      self.right = BinaryTree(new_value)
    else:
      if self.switch:
        self.left.insert(new_value)
      else:
        self.right.insert(new_value)

      self.switch = not self.switch

  def level_order_traversal(self):
    nodes = [self]
    level_order = []
    stage_nodes = []
    while nodes:
      for node in nodes:
        level_order.append(node.value)

        if node.left:
          stage_nodes.append(node.left)
        if node.right:
          stage_nodes.append(node.right)

      nodes = [] + stage_nodes
      stage_nodes = []

    return level_order

  def in_order_values(self):
    in_order = []
    def traverse(node):
      if not node.left:
        return in_order.append(node.value)

      if not node.right:
        return in_order.append(node.value)

      traverse(node.left)
      in_order.append(node.value)
      traverse(node.right)

    traverse(self)
    return in_order

  def pre_order_values(self):
    pre_order = []
    def traverse(node):
      pre_order.append(node.value)

      if node.left:
        traverse(node.left)

      if node.right:
        traverse(node.right)

    traverse(self)
    return pre_order

  def post_order_values(self):
    post_order = []
    def traverse(node):
      if not node.left:
        return post_order.append(node.value)

      if not node.right:
        return post_order.append(node.value)

      traverse(node.left)
      traverse(node.right)
      return post_order.append(node.value)

    traverse(self)
    return post_order

  def invert_in_place(self):
    nodes = [self]
    level_order = []
    stage_nodes = []

    while nodes:
      for node in nodes:
        if node.left:
          stage_nodes.append(node.left)
        if node.right:
          stage_nodes.append(node.right)

        hold = node.left
        node.left = node.right
        node.right = hold

      nodes = [] + stage_nodes
      stage_nodes = []

    return self

balanced_tree = BinaryTree()
balanced_tree.insert('A')
balanced_tree.insert('B')
balanced_tree.insert('C')
balanced_tree.insert('D')
balanced_tree.insert('E')
balanced_tree.insert('F')
balanced_tree.insert('G')
balanced_tree.insert('H')
balanced_tree.insert('I')
balanced_tree.insert('J')
balanced_tree.insert('K')
balanced_tree.insert('L')
balanced_tree.insert('M')
balanced_tree.insert('N')

in_order = balanced_tree.in_order_values()
pre_order = balanced_tree.pre_order_values()
post_order = balanced_tree.post_order_values()
level_order = balanced_tree.level_order_traversal()

assert balanced_tree.value == 'Root'
assert balanced_tree.left.value == 'A'
assert balanced_tree.right.value == 'B'
assert balanced_tree.left.left.value == 'C'
assert balanced_tree.right.left.value == 'D'
assert balanced_tree.left.right.value == 'E'
assert balanced_tree.right.right.value == 'F'
assert balanced_tree.left.left.left.value == 'G'
assert balanced_tree.right.left.left.value == 'H'
assert balanced_tree.left.right.left.value == 'I'
assert balanced_tree.right.right.left.value == 'J'
assert balanced_tree.left.left.right.value == 'K'
assert balanced_tree.right.left.right.value == 'L'
assert balanced_tree.left.right.right.value == 'M'
assert balanced_tree.right.right.right.value == 'N'

assert in_order == ['G', 'C', 'K', 'A', 'I', 'E', 'M', 'Root', 'H', 'D', 'L', 'B', 'J', 'F', 'N']
assert pre_order == ['Root', 'A', 'C', 'G', 'K', 'E', 'I', 'M', 'B', 'D', 'H', 'L', 'F', 'J', 'N']
assert post_order == ['G', 'K', 'C', 'I', 'M', 'E', 'A', 'H', 'L', 'D', 'J', 'N', 'F', 'B', 'Root']
assert level_order == ['Root', 'A', 'B', 'C', 'E', 'D', 'F', 'G', 'K', 'I', 'M', 'H', 'L', 'J', 'N']

unbalanced_tree = BinaryTree('A')
unbalanced_tree.left = BinaryTree('B')
unbalanced_tree.right = BinaryTree('C')
unbalanced_tree.left.left = BinaryTree('D')
unbalanced_tree.left.right = BinaryTree('E')
unbalanced_tree.left.right.left = BinaryTree('F')
unbalanced_tree.left.right.right = BinaryTree('G')

in_order = unbalanced_tree.in_order_values()
pre_order = unbalanced_tree.pre_order_values()
post_order = unbalanced_tree.post_order_values()
level_order = unbalanced_tree.level_order_traversal()

assert in_order == ['D', 'B', 'F', 'E', 'G', 'A', 'C']
assert level_order == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
assert pre_order == ['A', 'B', 'D', 'E', 'F', 'G', 'C']
assert post_order == ['D', 'F', 'G', 'E', 'B', 'C', 'A']

balanced_tree.invert_in_place()
assert balanced_tree.level_order_traversal() == ['Root', 'B', 'A', 'F', 'D', 'E', 'C', 'N', 'J', 'L', 'H', 'M', 'I', 'K', 'G']
print('All test passed =)')
