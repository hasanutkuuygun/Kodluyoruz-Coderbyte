inp = 'abcabc'
list1 = []
list1[:0] = inp
print(list1)
print(list1[1])

print(list1[2] in ['a','b'])