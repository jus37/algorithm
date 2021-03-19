import math
N = int(input())
keta = math.ceil(len(str(N)) / 2)
ans = 10000000
for i in range(1, 10**keta+1):
  if N % i == 0:
    j = N // i
    f = max(len(str(i)), len(str(j)))
    ans = min(ans, f)

print(ans)