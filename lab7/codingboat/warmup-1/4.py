def missing_char(str, n):
  result = ''
  for i in range(len(str)):
    if i != n:
      result+=str[i]
  return result