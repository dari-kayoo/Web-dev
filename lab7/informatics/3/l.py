n = input()
degree, ans = 0,  0
for i in n:
    ans += int(i) * 2 ** degree
    degree += 1 
print(ans)
