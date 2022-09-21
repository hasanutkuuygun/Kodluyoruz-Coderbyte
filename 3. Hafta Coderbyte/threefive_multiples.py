def ThreeFiveMultiples(num):
  sum = 0
  for i in range(1,num):
    if (i % 3 == 0) or (i % 5 == 0):
      sum += i

  # code goes here
  return sum

# keep this function call here 
print(ThreeFiveMultiples(input()))