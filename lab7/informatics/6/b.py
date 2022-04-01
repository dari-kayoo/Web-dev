def p(a, n):
    if (n < 0):
        return 1.0 / p(a, -n)
    if (n == 0):
        return 1
    else: 
        return a * p(a, n - 1)

a, n = map(int, input().split())
print(p(a, n))
