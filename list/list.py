def merge_lists(lst1, lst2):
    #     https://www.educative.io/module/lesson/data-structures-in-python/B137p8P75QW
    merge_l = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merge_l.append(lst1[i])
            i += 1
        else:
            merge_l.append(lst2[j])
            j += 1
    return merge_l + lst1[i:] + lst2[j:]


def merge_lists_inplace(lst1, lst2):
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            lst1.insert(i, lst2[j])
            i += 1
            j += 1
        else:
            i += 1
    print(lst1)
    return lst1 + lst2[j:]

def find_product(lst):
    prod = []
    for i in range(len(lst)):
        mul = 1
        for j in range(len(lst)):
            print(i, j)
            if i != j:
                mul = mul*lst[j]
                print("passed")
        print("Answer", mul)
        prod.append(mul)
    return prod

def find_first_unique(lst):
    for i in range(len(lst)):
        cur = lst[i]
        repeat = False
        for j in range(i+1, len(lst)):
            if cur == lst[i]:
                repeat = True
                break
        if not repeat:
            return cur
def find_minimum_value_in_list(arr):
    if len(arr) < 1:
        return None
    m = float('inf')
    for i in range(len(arr)):
        if arr[i] < m:
            m = arr[i]
    return m

if __name__ == '__main__':
    arr = []
    print(find_minimum_value_in_list(arr))