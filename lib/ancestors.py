#         Tree Graph
# 
#           _ 1 _
#          /  |  \
#         /   |   \
#        /    |    \
#       2     5     7 _____
#      / \     \     \     \ 
#     /   \     \     \     11
#    3     4     6     8
#                     / \
#                    /   \
#                   9     10

nodes = [[1, 2], [2, 3], [2, 4], [1, 5], [5, 6], [1, 7], [7, 8], [8, 9], [8, 10], [7, 11]]

def intersection(list_1, list_2):
  common_items = []
  for item_1 in list_1:
    for item_2 in list_2:
      if item_1 == item_2:
        common_items.append(item_1)
        break
  return common_items

def closest_ancestors(node_1, node_2):
  def traverse(node_1, node_2, ancestors={}):
    both_parents = []
    loop_switch = False
    for node in nodes:
      parent = node[0]
      child = node[1]

      if child == node_1 or child == node_2:
        both_parents.append(parent)
        if parent in ancestors:
          return parent
        ancestors[parent] = True
        if loop_switch:
          break
        loop_switch = True

    return traverse(both_parents[0], both_parents[1])
  return traverse(node_1, node_2)

def common_ancestors(node_1, node_2):
  def traverse(target_node, ancestors):
    for node in nodes:
      parent = node[0]
      child = node[1]

      if child == target_node:
        ancestors.append(parent)
        return traverse(parent, ancestors)
    return ancestors

  ancestors_1 = traverse(node_1, [])
  ancestors_2 = traverse(node_2, [])
  return intersection(ancestors_1, ancestors_2)

assert intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
assert intersection([1, 2, 3], [4, 5, 6]) == []
assert intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

assert closest_ancestors(3, 5) == 1
assert closest_ancestors(3, 4) == 2
assert closest_ancestors(9, 11) == 7

assert common_ancestors(3, 4) == [2, 1]
assert common_ancestors(9, 10) == [8, 7, 1]
assert common_ancestors(1, 7) == [] 
assert common_ancestors(3, 11) == [1]

print('All test passed =)')
