def intersection(list_a, list_b):
    shared_elements = []
    if not len(list_a) or not len(list_b):
        return shared_elements

    for a in list_a:
        for b in list_b:
            if a == b:
                shared_elements.append(a)
                break
    return shared_elements

assert intersection([], []) == []
assert intersection([1, 2, 3], []) == []
assert intersection([], [2, 3, 4]) == []
assert intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
assert intersection([1, 2, 3], [4, 5, 6]) == []
assert intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

# Should handle list of dictionaries
a = { 'name': 'ignacio', 'age': 35 }
b = { 'name': 'diego', 'age': 28 }
c = { 'name': 'antonio', 'age': 36 }
d = { 'name': 'alejandro', 'age': 27 }

assert intersection([a], [b, c, a]) == [a]
assert intersection([c], [b, a]) == []

print('All Tests passed =)')
