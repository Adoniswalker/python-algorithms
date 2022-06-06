# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
# Name it merge_lists(lst1, lst2).

def merge_lists(lst1, lst2):
    com_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            com_list.append(lst1[i])
            i += 1
        else:
            com_list.append(lst2[j])
            j += 1
    return com_list+lst1[i:]+lst2[j:]


list1 = []
list2 = [2,6,7,8]
print(merge_lists(list1, list2))