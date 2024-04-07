def partition_method_1(p_array, start, end):
    pivot = p_array[end]
    i = start - 1
    j = start
    while j < end:
        if p_array[j] <= pivot:
            i += 1
            p_array[i], p_array[j] = p_array[j], p_array[i]
        j += 1
    i += 1
    p_array[i], p_array[end] = p_array[end], p_array[i]
    return i


def partition_method_1_2(p_array, start, end):
    pivot = p_array[end]
    i = start - 1
    for j in range(start, end):
        if p_array[j] <= pivot:
            i += 1
            p_array[i], p_array[j] = p_array[j], p_array[i]
    i += 1
    p_array[i], p_array[end] = p_array[end], p_array[i]
    return i


v_array = [3, 2, 8, 9, 7, 4, 6, 5]
print(partition_method_1(v_array, 0, len(v_array) - 1))
