n = int(input())
cnt = 0
l = list(map(int, input().split()))
for i in l:
    if (i > 0):
        cnt += 1
print(cnt)