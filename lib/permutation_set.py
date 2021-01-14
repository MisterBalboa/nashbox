# Find a posible combination set with no repetition given a set length
#
# [a, b, c] ==> [ [a, b], [a, c], [b, c] ]
# 

deck_3 = ['A', 'B', 'C']
deck_4 = ['A', 'B', 'C', 'D']
deck_5 = ['A', 'B', 'C', 'D', 'E']

def get_combination_set(deck, set_length):
  sets = []
  def traverse(deck, acc):
    if len(acc) == set_length:
      return sets.append(acc)

    for index, item in enumerate(deck):
      traverse(deck[index + 1:], acc + [item])

  traverse(deck, [])
  return sets

get_combination_set_3 = get_combination_set(deck_3, 2)
assert len(get_combination_set_3) == 3
assert ['A','B'] in get_combination_set_3
assert ['A','C'] in get_combination_set_3
assert ['B','C'] in get_combination_set_3

get_combination_set_4 = get_combination_set(deck_4, 2)
assert len(get_combination_set_4) == 6
assert ['A','B'] in get_combination_set_4
assert ['A','C'] in get_combination_set_4
assert ['A','D'] in get_combination_set_4
assert ['B','C'] in get_combination_set_4
assert ['B','D'] in get_combination_set_4
assert ['C','D'] in get_combination_set_4

get_combination_set_5 = get_combination_set(deck_5, 2)
assert len(get_combination_set_5) == 10
assert ['A','B'] in get_combination_set_5
assert ['A','C'] in get_combination_set_5
assert ['A','D'] in get_combination_set_5
assert ['A','E'] in get_combination_set_5
assert ['B','C'] in get_combination_set_5
assert ['B','D'] in get_combination_set_5
assert ['B','E'] in get_combination_set_5
assert ['C','D'] in get_combination_set_5
assert ['C','E'] in get_combination_set_5
assert ['D','E'] in get_combination_set_5

get_combination_set_5 = get_combination_set(deck_5, 3)
assert len(get_combination_set_5) == 10
assert ['A','B','C'] in get_combination_set_5
assert ['A','B','D'] in get_combination_set_5
assert ['A','B','E'] in get_combination_set_5
assert ['A','C','D'] in get_combination_set_5
assert ['A','C','E'] in get_combination_set_5
assert ['A','D','E'] in get_combination_set_5
assert ['B','C','D'] in get_combination_set_5
assert ['B','C','E'] in get_combination_set_5
assert ['B','D','E'] in get_combination_set_5
assert ['C','D','E'] in get_combination_set_5
print('All test passed =)')
