INF = float('infinity')


n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a + [0]
b = [0] + [-INF] * (n - 1)
w = [-1] * n
for i in range(1, n):
    for j in range(max(i - k, 0), i):
        if b[j] + a[i] > b[i]:
            b[i] = b[j] + a[i]
            w[i] = j
print(b[n - 1])
r = []
t = n - 1
for i in range(n - 1, -1, -1):
    if i == t:
        r = [t + 1] + r
        t = w[i]
print(len(r) - 1)
print(*r)