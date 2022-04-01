n = int(input())
ans = "The {} number for the number {} is {}."
print(ans.format("next", n, n + 1))
print(ans.format("previous", n, n - 1))
