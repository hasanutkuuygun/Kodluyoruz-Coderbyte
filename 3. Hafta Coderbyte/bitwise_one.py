def BitwiseOne(strArr):
  result = []
  for i in range(len(strArr[0])):
    if (int(strArr[0][i]) == 0) and (int(strArr[1][i]) == 0):
      result.append('0')
    else:
      result.append('1')

  # code goes here
  return ''.join(result)
# keep this function call here 
print(BitwiseOne(input()))