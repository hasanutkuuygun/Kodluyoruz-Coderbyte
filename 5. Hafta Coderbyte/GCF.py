def GCF(arr):
  i = []
  j = []
  for a in range (1,arr[0]+1):
    if arr[0] % a == 0:
      i.append(a)
  for b in range (1,arr[1]+1):
    if arr[1] % b == 0:
      j.append(b)
    # code goes here
  return max(set(i).intersection(j))

# keep this function call here 
print(GCF(input()))