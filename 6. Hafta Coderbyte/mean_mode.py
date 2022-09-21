def MeanMode(arr):
  mean = sum(arr) / len(arr)
  mode = max(arr, key = arr.count)
  if mean == mode:return 1
  else: return 0
  # code goes here

# keep this function call here 
print(MeanMode(input()))