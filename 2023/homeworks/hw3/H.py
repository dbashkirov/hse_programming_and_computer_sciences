def way_reconstr(a, w, i):
    if w[i] == -1:
        return [a[i]]
    return way_reconstr(a, w, w[i]) + [a[i]]


n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
w = [-1] * n
for i in range(1, n):
    for j in range(i):
        if a[j] < a[i] and 1 + dp[j] > dp[i]:
            dp[i] = dp[j] + 1
            w[i] = j
m = max(dp)
for i in range(n):
    if dp[i] == m:
        temp = way_reconstr(a, w, i)
        print(len(temp))
        print(*temp)
        break