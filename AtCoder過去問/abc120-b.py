A,B,K = map(int,input().split())
count = 0
for i in reversed(range(1,min(A,B)+1)):
  if A % i == 0 and B % i == 0:
    count += 1
    if count == K:
      ans = i
print(ans)