import math

def cut_list_sections(full_list, n_sections):
    if not full_list:
        return []

    if n_sections == 1:
        return full_list

    if len(full_list) == n_sections:
        return [ [e] for e in full_list]

    final = []
    position_index = 0
    last_index = len(full_list) - 1
    portions_left = n_sections

    while position_index < len(full_list):
        remains = full_list[position_index:(last_index + 1)]
        if len(remains) == portions_left:
            final += [ [e] for e in remains ]
            break

        step = math.ceil(len(remains) / portions_left)
        section = remains[0:step]
        final.append(section)
        portions_left -= 1
        position_index += step

    return final

assert cut_list_sections([], 5) == []
assert cut_list_sections([1, 2, 3, 4, 5, 6], 1) == [1, 2, 3, 4, 5, 6]
assert cut_list_sections([1, 2, 3, 4, 5, 6], 2) == [[1, 2, 3], [4, 5, 6]]
assert cut_list_sections([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
assert cut_list_sections([1, 2, 3, 4, 5, 6], 4) == [[1, 2], [3, 4], [5], [6]]
assert cut_list_sections([1, 2, 3], 2) == [[1, 2], [3]]
assert cut_list_sections([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
assert cut_list_sections([1, 2, 3, 4], 4) == [[1], [2], [3], [4]]
assert cut_list_sections([1, 2, 3, 4], 5) == [[1], [2], [3], [4]]
assert cut_list_sections([1, 2], 5) == [[1], [2]]
print('All test passed =)')

