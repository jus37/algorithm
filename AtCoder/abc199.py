# A
A,B,C = map(int, input().split())

if A**2 + B**2 < C**2:
  print('Yes')
else:
  print('No')

# B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num = []
for n in range(1,1001):
  num.append(n)
out = []
for n in range(N):
  for o in range(len(num)):
    if not (A[n] <= num[o] <= B[n]):
      out.append(num[o])

for n in range(len(out)):
  if out[n] in num:
    num.remove(out[n])

print(len(num))

# C（TLE）
N = int(input())
S = list(input())
Q = int(input())

for _ in range(Q):
  T,A,B = map(int, input().split())
  if T == 1:
    A -= 1
    B -= 1
    S[A], S[B] = S[B], S[A]
  else:
    S[0:N], S[N:N*2] = S[N:N*2], S[0:N]


print(''.join(S))