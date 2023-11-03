n = int(input())
s = input()
ones, zeros = 0, 0
for c in s:
    if c == '0':
        zeros += 1
    else:
        ones += 1
if zeros != ones:
    print(1)
    print(s)
else:
    print(2)
    print(s[0], s[1:])