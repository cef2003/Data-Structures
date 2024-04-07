def partition_method_2(p_array, start, end):
    pivot = p_array[start]
    i = start
    j = end + 1
    while j > i:
        while True:
            i += 1
            if p_array[i] > pivot:
                break
        while True:
            j -= 1
            if p_array[j] <= pivot:
                break
        if j > i:
            p_array[i], p_array[j] = p_array[j], p_array[i]
    p_array[j], p_array[start] = p_array[start], p_array[j]
    return j


v_array = [3, 2, 8, 9, 7, 4, 6, 5]
print(partition_method_2(v_array, 0, len(v_array) - 1))
