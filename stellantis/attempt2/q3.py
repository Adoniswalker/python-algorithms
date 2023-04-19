def fib(n):
    values = [0, 1]
    for i in range(2, n):
        value = values[i-1] + values[i-2]
        values.append(value)
    print(values)
    return values[n-1]


if __name__ == '__main__':
    print(fib(0))