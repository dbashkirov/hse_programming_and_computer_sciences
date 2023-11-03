n = int(input())
x_sum, y_sum, z_sum = 0, 0, 0
for _ in range(n):
    a = list(map(int, input().split()))
    x_sum += a[0]
    y_sum += a[1]
    z_sum += a[2]
if x_sum == y_sum == z_sum == 0:
    print("YES")
else:
    print("NO")
