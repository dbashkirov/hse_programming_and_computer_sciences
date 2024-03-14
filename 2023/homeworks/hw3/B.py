def f(t):
    a = t // min(x, y)
    b = (t - min(x, y)) // max(x, y)
    return a + b >= n


def bin_search(l, r):
    while r - l > 1:
        m = (l + r) // 2
        if f(m):
            r = m
        else:
            l = m + 1
    if f(l):
        return l
    return r


n, x, y = map(int, input().split())
print(bin_search(min(x, y), min(x, y) * n))