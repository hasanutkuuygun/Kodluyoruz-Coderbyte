def WildcardCharacters(strParam):
  x , y = strParam.split()
  # print('x =',x)
  # print('y =',y)
  plus = x.count('+')
  asterisk  = x.count('*')

  if '{' in x:
    N = int(x[x.index('{') + 1])
    if (plus + 3 * (asterisk-1) + N) == len(y):
      return 'true'
    else:
      return 'false'



  else:
    if (plus + 3 * asterisk) == len(y):
      return 'true'
    else:
      return 'false'
  # code goes here

# keep this function call here 
print(WildcardCharacters(input()))