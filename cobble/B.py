def solution(S):
    f = [0] * 26

    n = len(S)

    for i in range(n):
        f[ord(S[i]) - ord('a')] += 1

    c = 0

    for i in range(26):
        if f[i] % 2:
            c += 1

    if c == 0 or c == 1:
        return 0

    else:
        return c - 1


if __name__ == "__main__":
    # print(solution("ervervige"))
    print(solution("abefbac"))
    print(solution("aaabab"))
