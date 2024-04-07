def merge_sort_recursive(p_array):
    if len(p_array) < 2:
        return p_array
    else:
        m = len(p_array) // 2
        return merge(merge_sort_recursive(p_array[:m]), merge_sort_recursive(p_array[m:]))


def merge(p_array_1, p_array_2):
    if not p_array_1:
        return p_array_2
    elif not p_array_2:
        return p_array_1
    elif p_array_1[0] < p_array_2[0]:
        return [p_array_1[0]] + merge(p_array_1[1:], p_array_2)
    else:
        return [p_array_2[0]] + merge(p_array_1, p_array_2[1:])


v_array = [8, 3, 5, 17, 10, 11, 15]
print("Before: ", v_array)
v_array = merge_sort_recursive(v_array)
print("After: ", v_array)
