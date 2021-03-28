# A
s = input()
print(s[1]+s[2]+s[0])

# B
H,W,X,Y = map(int, input().split())
S = []
for i in range(H):
  s = input()
  S.append(s)

X -= 1
Y -= 1

ans = 0

x,y = X,Y
while x >=0:
  if S[x][y] == '#':
    break
  if S[x][y] == '.':
    ans += 1
    x -= 1

x,y = X,Y
while x < H:
  if S[x][y] == '#':
    break
  if S[x][y] == '.':
    ans += 1
    x += 1

x,y = X,Y
while y >=0:
  if S[x][y] == '#':
    break
  if S[x][y] == '.':
    ans += 1
    y -= 1

x,y = X,Y
while y < W:
  if S[x][y] == '#':
    break
  if S[x][y] == '.':
    ans += 1
    y += 1

print(ans-3)


# C
N = int(input())
A = list(map(int, input().split()))

ans = 10*100

for i in range(2**(N-1)):
  orsum = 0
  xorsum = 0
  for j in range(N):
    orsum = orsum | A[j]
    if ((i>>j) & 1) or j == N-1:
      xorsum = xorsum ^ orsum
      orsum = 0
  ans = min(ans,xorsum)

print(ans)