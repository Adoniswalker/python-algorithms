def main(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr =  [5, 1, 4, 2, 8]
    main(arr)
    print(arr)

