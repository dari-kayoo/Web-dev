n = int(input())
l = list(map(int, input().split()))
for i in range(0, len(l) - 1):
    if (l[i + 1] * l[i] > 0):
        print("YES")
        break
else:
    print("NO")