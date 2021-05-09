# A
N = int(input())
if N % 100 != 0:
  print(N//100 +1)
else:
  print(N//100)


# B

N,K = map(int, input().split())

for _ in range(K):
  if N % 200 == 0:
    N //= 200
  else:
    N = int(str(N)+str(200))

print(N)

# C
import itertools
N = int(input())
A = list(map(int, input().split()))
ans = 0

for n in itertools.combinations(A,2):
  cal = n[0] - n[1]
  if cal % 200 == 0:
    ans += 1

print(ans)

