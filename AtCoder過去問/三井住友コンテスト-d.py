import itertools
N = int(input())
s = list(input())

ans = 0
judge = []
while len(s) >= 3:
  first = s.pop(0)
  if first in judge:
    continue
  combi = list(itertools.combinations(s, 2))
  combi = sorted(set(combi), key = combi.index)
  ans += len(combi)
  judge.append(first)

print(ans)

N = int(input())
S = list(input())
ans = 0
for i in range(1000):
  if i < 10:
    i0 = "0"
    i1 = "0"
    i2 = str(i)
  elif i < 100:
    i0 = "0"
    i1 = str(i)[0]
    i2 = str(i)[1]
  else:
    i0 = str(i)[0]
    i1 = str(i)[1]
    i2 = str(i)[2]
  if i0 in S:
    p1 = S.index(i0)
    if i1 in S[p1+1:N]:
      p2 = S[p1+1:N].index(i1) + (p1+1)
      if i2 in S[p2+1:N]:
        ans += 1

print(ans)
