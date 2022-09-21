def PentagonalNumber(num):
  if num == 1:
    result = 1
  elif num == 2:
    result = 6
  else:
    result = 6
    for i in range(3, num + 1):
      result += (5 + (i - 2) * 5)

  # code goes here
  return result

# keep this function call here 
print(PentagonalNumber(input()))