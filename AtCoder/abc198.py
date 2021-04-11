# A
n = int(input())
print(n-1)
# B
n = input()
result = n
for i in reversed(range(len(n))):
  if n[i] == '0':
    result = '0' + result
  else:
    break

if result == result[::-1]:
  print('Yes')
else:
  print('No')
# C