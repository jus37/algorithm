# A
M,H = map(int, input().split())
if H % M ==0:
  print("Yes")
else:
  print("No")

# B
# B
A,B,W = map(int,input().split())

res = False
min = 0
max = 0


q = W*1000 // A
mod = W*1000 % A
if mod == 0:
  res = True
else:
  while res == False or q > 0:
    q -= 1
    mod += A
    for i in range(A, B+1):
      if mod % i == 0:
        q += mod // i
        res = True

if res:
  max = q
else:
  print("UNSATISFIABLE")
  exit()

q = W*1000 // B
mod = W*1000 % B
res = False
if mod == 0:
  res = True
else:
  while res == False or q > 0:
    q -= 1
    mod += B
    for i in range(A, B+1):
      if mod % i == 0:
        q += mod // i
        res = True

if res:
  min = q
else:
  print("UNSATISFIABLE")
  exit()

print(min,max)

# C
N = int(input())


N = str(N)
keta = len(N)-1

ans = 0
i = 3
kanma = 0
while keta >i:
  if i % 3 ==0:
    kanma +=1
  ans += kanma*(10**i*9)
  i += 1

if i % 3 == 0:
  kanma += 1

N = int(N)
if N>= 1000:
  ans += (N-10**i+1)*kanma

print(ans)

