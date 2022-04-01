def monkey_trouble(a_smile, b_smile):
  if a_smile == 1 and b_smile == 1:
    return True
  elif a_smile == 0 and b_smile == 0:
    return True
  elif a_smile == 1 and b_smile == 0:
    return False
  return False