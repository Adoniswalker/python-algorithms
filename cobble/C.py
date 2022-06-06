def d_sum(n):
    sum = 0
    while (n):
        sum += (n % 10)
        n = n // 10
    return sum


def solution(A):
    n = len(A)
    m = {}
    ans = -1
    p_i = 0
    p_j = 0
    for i in range(n):

        t = d_sum(A[i])

        if t not in m:
            m[t] = 0

        if m[t] != 0:
            if A[i] + m[t] > ans:
                p_i = A[i]
                p_j = m.get(t)
                ans = p_i + p_j

        m[t] = max(A[i], m[t])
    return ans


if __name__ == "__main__":
    # print(solution("ervervige"))
    A = [51, 71, 17, 42]
    # A = [42, 33, 60]
    # A = [51, 32, 43]
    print(solution(A))
