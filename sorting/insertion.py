def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]#11
        j = i-1#0
        while arr[j] > temp and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp

def insertion_recursive(arr, i):
    if i==1: return 0

array = [12, 11, 13, 5, 6]
insertion_sort(array)
print(array)
# Time Complexity: O(n^2
# Auxiliary Space: O(1)