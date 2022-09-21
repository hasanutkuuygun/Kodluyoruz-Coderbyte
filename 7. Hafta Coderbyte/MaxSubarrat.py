def MaxSubarray(arr):
  sums = []
  for i in range(len(arr)):
    subsum = arr[i]
    # print('----------',subsum)
    for y in range(i+1, len(arr)):
      subsum += arr[y]
      # print(arr[i], arr[y], subsum)
      sums.append(subsum)
      # print(sums)
      
    



  # code goes here
  return max(sums)

# keep this function call here 
print(MaxSubarray(input()))