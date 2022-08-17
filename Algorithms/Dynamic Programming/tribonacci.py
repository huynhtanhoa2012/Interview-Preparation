def tribonacci(n: int) -> int:
    t = [0] * 38
    t[0] = 0
    t[1] = 1
    t[2] = 1

    for i in range(3, n):
        t[i] = t[i-3] + t[i-2] + t[i-1]

    return t[n]