def main(A):
    k = {}

    for i in range(0, len(A)):
        if A[i] in k.keys():
            k[A[i]] += 1
        else:
            k[A[i]] = 1
        i += 1
    m = 0
    for j, s in k.items():
        if j == s and s > m:
            m = s
    return m


if __name__ == "__main__":
    # A = [3, 8, 2, 3, 3, 2]
    # A = [7, 1, 2, 8, 2]
    # A = [3, 1, 4, 1, 5]
    A = [5, 5, 5, 5, ]
    main(A)
