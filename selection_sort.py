def min(p_array):
    index = 0
    index_min = 0
    while index < len(p_array) - 1:
        if p_array[index] < p_array[index_min]:
            index_min = index
        index += 1
    return index_min


def max(p_array):
    index = 0
    index_max = 0
    while index < len(p_array) - 1:
        if p_array[index] > p_array[index_max]:
            index_max = index
        index += 1
    return index_max


def selection_sort(p_array):
    marker = len(p_array)
    while marker > 0:
        index_max = max(p_array)
        p_array[marker - 1], p_array[index_max] = p_array[index_max], p_array[marker - 1]
        marker -= 1


v_array = [7, 6, 1, 5, 16, 27, 33, 22, 3, 9]
print("Max element is ", v_array[max(v_array)], " at index ", max(v_array))
print("Min element is ", v_array[min(v_array)], " at index ", min(v_array))
print("Before sorting: ")
print(v_array)
selection_sort(v_array)
print("After sorting: ")
print(v_array)