def bubble_sort(p_array):
    permutation = True
    while permutation:
        permutation = False
        for i in range(0, len(p_array) - 1):
            if p_array[i] > p_array[i+1]:
                permutation = True
                p_array[i], p_array[i+1] = p_array[i+1], p_array[i]


v_array = [7, 6, 1, 5, 16, 27, 33, 22, 3, 9]
print("Before: ", v_array)
bubble_sort(v_array)
print("After: ", v_array)
