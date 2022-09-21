def StockPicker(arr):
  i = len(arr) - 1
  final_profit = []
  while 0 <= i:
    profit = []
    for j in range(0,i):
      profit.append(arr[i] - arr[j])
      final_profit.append(max(profit))
    i -= 1
  
  max_profit = max(final_profit)
  
  if max_profit > 0: return max_profit
  else: return -1

  # code goes here

# keep this function call here 
print(StockPicker(input()))