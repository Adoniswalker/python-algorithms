def sum_reccusive(array, n):
    if n == len(array):
        return 0
    return array[n]+sum_reccusive(array, n+1)

def sum_of_list(array):
    return sum_reccusive(array, 0)

print(sum_of_list([1,5,7,-1]))