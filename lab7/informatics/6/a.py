def min(a, b, c, d):
    mini = a
    if b < mini:
        mini = b
    if c < mini:
        mini = c
    if d < mini:
        mini = d
    return mini
    

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))