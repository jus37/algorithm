import itertools
import math

N = int(input())
mp = []
for _ in range(N):
  s = list(map(int, input().split()))
  mp.append(s)
ans = 0
for lis in itertools.permutations(mp,N):
  for i in range(1, len(lis)):
    ans += math.sqrt((lis[i][0]-lis[i-1][0])**2 + (lis[i][1]-lis[i-1][1])**2)

print(ans/math.factorial(N))