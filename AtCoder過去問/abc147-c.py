N =int(input())
sum = []
opis = []
for _ in range(N):
  a = int(input())
  sum.append(a)
  opi = []
  for _ in range(a):
    b = list(map(int, input().split()))
    opi.append(b)
  opis.append(opi)

ans = 0
for n in range(2**N):
  judge = True
  for hum in range(N):
    if n & 1<<hum > 0:
      for op in opis[hum]:
        if op[1] == 0 and n & 1<<(op[0]-1) > 0:
          judge = False
        if op[1] == 0 and n & 1<<(op[0]-1) <= 0:
          judge = False
  if judge:
    ans = max(ans,str(bin(n)).count("1"))

print(ans)

