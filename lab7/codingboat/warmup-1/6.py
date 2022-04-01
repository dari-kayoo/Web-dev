def parrot_trouble(talking, hour):
  if talking == 1: 
    if hour < 7 or hour > 20:
      return True
  return False