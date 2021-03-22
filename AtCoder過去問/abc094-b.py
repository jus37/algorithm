N = int(input())
result = "No"
for i in range(1, 10):
  for j in range(1, 10):
    if N == i*j:
      result = "Yes"
      break

print(result)
