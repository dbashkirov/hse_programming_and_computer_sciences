EPS = 10 ** -4
PR_EPS = 10 ** -6


def f(x):
    return ((1 - a) ** 2 + x ** 2) ** .5 / v_p + (a ** 2 + (1 - x) ** 2) ** .5 / v_f


def tern_search(l, r):
    for _ in range(int((r - l) / EPS)):
        m1 = (r + l) / 2 - PR_EPS
        m2 = (r + l) / 2 + PR_EPS
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return r


v_p, v_f = map(int, input().split())
a = float(input())
print(tern_search(0, 1))