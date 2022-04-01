from math import floor

n = int(input())
l = list(map(int, input().split()))
for i in range(0, n): 
    if (i == floor(n / 2)):
        break
    tmp = l[i]
    l[i] = l[n - 1 - i]
    l[n - i - 1] = tmp
for i in l:
    print(i, end=' ')
