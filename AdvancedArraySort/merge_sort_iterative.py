def merge(p_array_1, p_array_2):
    index_array_1, index_array_2, size_array_1, size_array_2 = 0, 0, len(p_array_1), len(p_array_2)
    v_array = []
    while index_array_1 < size_array_1 and index_array_2 < size_array_2:
        if p_array_1[index_array_1] < p_array_2[index_array_2]:
            v_array.append(p_array_1[index_array_1])
            index_array_1 += 1
        else:
            v_array.append(p_array_2[index_array_2])
            index_array_2 += 1

    if index_array_1 == size_array_1:
        v_array.extend(p_array_2[index_array_2:])
    if index_array_2 == size_array_2:
        v_array.extend(p_array_1[index_array_1:])

    return v_array


def merge_sort_iterative(p_array):
    if len(p_array) < 2:
        return p_array
    else:
        m = len(p_array) // 2
        return merge(merge_sort_iterative(p_array[:m]), merge_sort_iterative(p_array[m:]))


v_array = [8, 3, 5, 17, 10, 11, 15]
print("Before: ", v_array)
v_array = merge_sort_iterative(v_array)
print("After: ", v_array)
