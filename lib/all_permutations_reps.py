#
#             __A B__
#            /       \
#           /         \
#          A           B
#         / \         / \
#        /   \       /   \
#       AA   AB     BB   BA
#
#
#
#
#                              _________________________________________ A B C __________________________________________
#                             /                                             |                                            \ 
#                            /                                              |                                             \ 
#               ____________A_____________                      ____________B_____________                     ____________C_____________          
#              /            |             \                    /            |             \                   /            |             \         
#             /             |              \                  /             |              \                 /             |              \        
#         __AA__          __AB__          __AC__          __BA__          __BB__          __BC__         __CA__          __CB__          __CC__    
#        /   |  \        /   |  \        /   |  \        /   |  \        /   |  \        /   |  \       /   |  \        /   |  \        /   |  \   
#       /    |   \      /    |   \      /    |   \      /    |   \      /    |   \      /    |   \     /    |   \      /    |   \      /    |   \  
#     AAA   AAB  AAC  ABA   ABB  ABC  ACA   ACB  ACC BAA   BAB  BAC   BBA   BBB  BBC  BCA   BCB  BCC CAA   CAB  CAC  CBA   CBB  CBC  CCA   CCB  CCC 
#
#
#


deck_2 = ['A', 'B']
deck_3 = ['A', 'B', 'C']
deck_4 = ['A', 'B', 'C', 'D']

# Recursive Approach
def get_all_permutations_reps(deck):
  all_permutations = []
  def traverse(deck, acc):
    if len(acc) == len(deck):
      return all_permutations.append(acc)

    for index, item in enumerate(deck):
      traverse(deck, acc + [item])

  traverse(deck, [])
  return all_permutations

# # Math approach
# def get_all_permutations_reps(deck):
#   main_index = 0
#   all_permutations = []
#   base = len(deck)
#   power = len(deck)
#   total_permutations = len(deck) ** power
#   while main_index < total_permutations:
#     combo = []
# 
#     for power_index in range(0, power):
#       unit_index = base ** power_index
#       combo.append(deck[unit_index])
# 
#     all_permutations.append(combo)
#   return all_permutations

print('all perms: {}'.format(get_all_permutations_reps(deck_2)))
# all_permutation_reps_2 = get_all_permutations_reps(deck_2)
# assert len(all_permutation_reps_2) == 4
# assert ['A','A'] in all_permutation_reps_2
# assert ['A','B'] in all_permutation_reps_2
# assert ['B','A'] in all_permutation_reps_2
# assert ['B','B'] in all_permutation_reps_2
# 
# all_permutation_reps_3 = get_all_permutations_reps(deck_3)
# assert len(all_permutation_reps_3) == 27
# assert ['A','A','A'] in all_permutation_reps_3
# assert ['A','A','B'] in all_permutation_reps_3
# assert ['A','A','C'] in all_permutation_reps_3
# assert ['A','B','A'] in all_permutation_reps_3
# assert ['A','B','B'] in all_permutation_reps_3
# assert ['A','B','C'] in all_permutation_reps_3
# assert ['A','C','A'] in all_permutation_reps_3
# assert ['A','C','B'] in all_permutation_reps_3
# assert ['A','C','C'] in all_permutation_reps_3
# assert ['B','A','A'] in all_permutation_reps_3
# assert ['B','A','B'] in all_permutation_reps_3
# assert ['B','A','C'] in all_permutation_reps_3
# assert ['B','B','A'] in all_permutation_reps_3
# assert ['B','B','B'] in all_permutation_reps_3
# assert ['B','B','C'] in all_permutation_reps_3
# assert ['B','C','A'] in all_permutation_reps_3
# assert ['B','C','B'] in all_permutation_reps_3
# assert ['B','C','C'] in all_permutation_reps_3
# assert ['C','A','A'] in all_permutation_reps_3
# assert ['C','A','B'] in all_permutation_reps_3
# assert ['C','A','C'] in all_permutation_reps_3
# assert ['C','B','A'] in all_permutation_reps_3
# assert ['C','B','B'] in all_permutation_reps_3
# assert ['C','B','C'] in all_permutation_reps_3
# assert ['C','C','A'] in all_permutation_reps_3
# assert ['C','C','B'] in all_permutation_reps_3
# assert ['C','C','C'] in all_permutation_reps_3
# 
# all_permutation_reps_4 = get_all_permutations_reps(deck_4)
# assert len(all_permutation_reps_4) == 256
# print('All test passed =)')
