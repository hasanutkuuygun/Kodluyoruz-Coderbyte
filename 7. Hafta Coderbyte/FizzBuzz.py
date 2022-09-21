def FizzBuzz(num):
  result = ''
  for i in range(1,num+1):
    if (i % 3 == 0) and (i % 5 == 0):
      result += 'FizzBuzz '
    elif (i % 3 == 0):
      result += 'Fizz '
    elif (i % 5 == 0):
      result += 'Buzz '
    else:
      result += (str(i) + ' ')

  # code goes here
  return result

# keep this function call here 
print(FizzBuzz(input()))