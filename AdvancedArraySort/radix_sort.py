def counting_sort(p_array, place):
    output = [0] * len(p_array)
    count = [0] * 10
    for i in range(0, len(p_array)):
        index = p_array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = len(p_array) - 1
    while i >= 0:
        index = p_array[i] // place
        output[count[index % 10] - 1] = p_array[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(p_array)):
        p_array[i] = output[i]


def radix_sort(p_array):
    max_num = max(p_array)
    place = 1
    while max_num // place > 0:
        counting_sort(p_array, place)
        place *= 10
        

v_array = [54, 89, 160, 37, 634, 234]
print("Before: ", v_array)
radix_sort(v_array)
print("After: ", v_array)