def LargestPair(num):
  num = str(num)
  numbers = []
  for i in range(len(num)-1):
    numbers.append(int(num[i]+num[i+1]))
    maks = max(numbers)
  # code goes here
  return maks

# keep this function call here 
print(LargestPair(input()))