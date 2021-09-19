def selection_sort(arr):
    for i in range(len(arr)):
        j = i + 1
        min_idx = i
        while j < len(arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
            j += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


array = [64, 25, 12, 22, 11]
selection_sort(array)
print(array)
# Time Complexity: O(n2) as there are two nested loops.
# Auxiliary Space: O(1)
# mi = array[0]

# for i in range(len(array)):
#     if array[i]<mi:
#         mi = array[i]


# print(mi)
