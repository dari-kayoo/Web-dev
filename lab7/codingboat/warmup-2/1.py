def sleep_in(weekday, vacation):
  if weekday == 0 and vacation == 0:
    return True
  elif weekday == 1 and vacation == 0:
    return False
  elif weekday == 0 and vacation == 1:
    return True
  return True