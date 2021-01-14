def is_same_combination(list_1, list_2):
  if len(list_1) != len(list_2):
    raise Exception('lists are not the same length')

  list_of_lists = [
    isinstance(e, list) for e in list_1 \
      and isinstance(e, list) for e in list_2
  ]

  for item_1 in list_1:
    all_in = False
    for item_2 in list_2:
      if item_1 == item_2:
        all_in = True
    if not all_in:
      return False
  return True
