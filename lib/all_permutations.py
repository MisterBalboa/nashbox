#
#            A B
#            / \
#           /   \
#          A     B
#          |     |
#         AB     BA
#
#
#
#
#          ________________ A B C _______________
#         /                   |                   \                    
#        /                    |                    \                   
#     __A__                ___B___               __C__
#    /     \              /       \             /     \        
#   /       \            /         \           /       \       
# AB         AC        BA           BC       CA         CB     
#  |          |        |             |       |          |
#  |          |        |             |       |          |
# ABC        ACB      BAC           BCA     CAB        CBA  
#
#
#
#
#
#                      _______________________________________________ A B C D____________________________________________________
#                     /                                     /                               \                                     \   
#                    /                                     /                                 \                                     \  
#         ________ A_________                  ________ B_________                   ________ C________                    ________ D________
#        /         |         \                /         |         \                 /         |         \                 /         |         \
#       /          |          \              /          |          \               /          |          \               /          |          \
#     AB          AC           AD          BA          BC           BD           CA          CB           CD           DA          DB           DC
#    /  \        /  \         /  \        /  \        /  \         /  \         /  \        /  \         /  \         /  \        /  \         /  \
#   /    \      /    \       /    \      /    \      /    \       /    \       /    \      /    \       /    \       /    \      /    \       /    \
# ABC    ABD  ACB    ACD   ADB    ADC  BAC    BAD  BCA    BCD   BDA    BDC   CAB    CAD  CBA    CBD   CDA    CDB   DAB    DAC  DBA    DBC   DCA    DCB
#  |      |    |      |     |      |    |      |    |      |     |      |     |      |    |      |     |      |     |      |    |      |     |      |
#  |      |    |      |     |      |    |      |    |      |     |      |     |      |    |      |     |      |     |      |    |      |     |      |
# ABCD   ABDC ACBD   ACDB  ADBC   ADCB BACD   BADC BCAD   BCDA  BDAC   BDCA  CABD   CADB CBAD   CBDA  CDAB   CDBA  DABC   DACB DABC   DBCA  DCAB   DCBA
#


deck_2 = ['A', 'B']
deck_3 = ['A', 'B', 'C']
deck_4 = ['A', 'B', 'C', 'D']

def get_all_permutations(deck):
  total = []
  def sub_routine(deck, acc=[]):
    if not deck:
      return total.append(acc)

    for element in deck:
      sub_routine(
        [
          remain
          for remain in deck
          if remain is not element
        ],
        acc + [ element ]
      )

  sub_routine(deck)
  return total

all_permutations_2 = get_all_permutations(deck_2)
assert len(all_permutations_2) == 2
assert ['A','B'] in all_permutations_2
assert ['B','A'] in all_permutations_2

all_permutations_3 = get_all_permutations(deck_3)
assert len(all_permutations_3) == 6
assert ['A','B','C'] in all_permutations_3
assert ['A','C','B'] in all_permutations_3
assert ['B','A','C'] in all_permutations_3
assert ['B','C','A'] in all_permutations_3
assert ['C','A','B'] in all_permutations_3
assert ['C','B','A'] in all_permutations_3

all_permutations_4 = get_all_permutations(deck_4)
assert len(all_permutations_4) == 24
assert ['A','B','C','D'] in all_permutations_4
assert ['A','B','D','C'] in all_permutations_4
assert ['A','C','B','D'] in all_permutations_4
assert ['A','C','D','B'] in all_permutations_4
assert ['A','D','B','C'] in all_permutations_4
assert ['A','D','C','B'] in all_permutations_4

assert ['B','A','C','D'] in all_permutations_4
assert ['B','A','D','C'] in all_permutations_4
assert ['B','C','A','D'] in all_permutations_4
assert ['B','C','D','A'] in all_permutations_4
assert ['B','D','A','C'] in all_permutations_4
assert ['B','D','C','A'] in all_permutations_4

assert ['C','A','B','D'] in all_permutations_4
assert ['C','A','D','B'] in all_permutations_4
assert ['C','B','A','D'] in all_permutations_4
assert ['C','B','D','A'] in all_permutations_4
assert ['C','D','A','B'] in all_permutations_4
assert ['C','D','B','A'] in all_permutations_4

assert ['D','A','B','C'] in all_permutations_4
assert ['D','A','C','B'] in all_permutations_4
assert ['D','B','A','C'] in all_permutations_4
assert ['D','B','C','A'] in all_permutations_4
assert ['D','C','A','B'] in all_permutations_4
assert ['D','C','B','A'] in all_permutations_4

print('All test passed =)')
