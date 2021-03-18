N = int(input())
ans = 0
for i in range(1, N+1):
  result = 0
  for j in range(1, N+1):
    if i % j == 0:
      result += 1
  if result == 8:
    ans += 1

print(ans)