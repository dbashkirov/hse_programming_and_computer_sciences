INF = float('infinity')


def way_reconstr(w, i, j):
    if w[i][j] == '':
        return ''
    elif w[i][j] == 'U':
        return way_reconstr(w, i - 1, j) + 'D'
    else:
        return way_reconstr(w, i, j - 1) + 'R'


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
w = [[''] * m for _ in range(n)]
for i in range(1, n):
    a[i][0] += a[i - 1][0]
    w[i][0] = 'U'
for j in range(1, m):
    a[0][j] += a[0][j - 1]
    w[0][j] = 'L'
for i in range(1, n):
    for j in range(1, m):
        if a[i - 1][j] > a[i][j - 1]:
            a[i][j] += a[i - 1][j]
            w[i][j] = 'U'
        else:
            a[i][j] += a[i][j - 1]
            w[i][j] = 'L'
print(a[-1][-1])
print(way_reconstr(w, n - 1, m - 1))