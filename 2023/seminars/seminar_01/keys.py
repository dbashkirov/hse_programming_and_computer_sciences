x = input()
y = input()
z = ""
exist = True
n = len(x)
for i in range(n):
    if y[i] > x[i]:
        exist = False
        break
    else:
        z += y[i]
if exist:
    print(z)
else:
    print(-1)
