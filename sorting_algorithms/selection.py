
def main(arr):
    for i in range(len(arr)):
        s = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[s]:
                s = j
        arr[s], arr[i] = arr[i], arr[s]


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    main(arr)
    print(arr)