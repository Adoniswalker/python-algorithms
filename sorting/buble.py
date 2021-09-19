def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            print(arr)
        print("\n")
        if not swapped:
            break


def bubble_recursive(arr, swapped, n):
    if not swapped: return
    if n == 0: return
    swapped = False
    for j in range(n):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    bubble_recursive(arr, swapped, n - 1)


array = [8, 7, 6, 5, 4, 3, 2, 1, 0]
# bubble_sort(array)
bubble_recursive(array, True, len(array)-1)
print(array)
# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
# Auxiliary Space: O(1)
