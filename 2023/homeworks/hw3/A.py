from collections import Counter

DICT_SIZE = ord('z') - ord('a') + 1

n, m = list(map(int, input().split()))
s = str(input())
t = str(input())
count_cards = Counter(t)
cnt = 0

i, j = 0, 0
count_string = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
while i < n:
    substring_is_ok = True
    while j < n and substring_is_ok:
        if count_string[s[j]] + 1 > count_cards[s[j]]:
            substring_is_ok = False
        else:
            count_string[s[j]] += 1
            j += 1
    cnt += (j - i)
    count_string[s[i]] -= 1
    i += 1

print(cnt)
