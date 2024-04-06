def bubble_sort_recursive(p_array):
    permutation = False
    for i in range(0, len(p_array) - 1):
        if p_array[i] > p_array[i+1]:
            permutation = True
            p_array[i], p_array[i+1] = p_array[i+1], p_array[i]
    if permutation:
        return bubble_sort_recursive(p_array)
    else:
        return p_array


v_array = [7, 6, 1, 5, 16, 27, 33, 22, 3, 9]
print("Before: ", v_array)
bubble_sort_recursive(v_array)
print("After: ", v_array)
