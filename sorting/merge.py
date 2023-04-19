
def merge(a, b):
    i, j = 0, 0
    ar = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ar.append(a[i])
            i += 1
        else:
            ar.append(b[j])
            j += 1
    ar = ar+a[i:] + b[j:]
    return ar


def merge_sorted(array):
    mid = len(array)/2
    


if __name__ == '__main__':
    arr1 = [83, 20, 9, 50, 115, 61, 17]
    print(merge(arr1))
