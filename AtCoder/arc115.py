# A
# TLE
import itertools

N,M = map(int, input().split())
lis = []
for _ in range(N):
  s = input()
  lis.append(s)

combi = list(itertools.combinations(lis, 2))

ans = 0
for i in combi:
  if str(bin(int(i[0],2) ^ int(i[1],2))).count("1") % 2 == 1:
    ans += 1

print(ans)
