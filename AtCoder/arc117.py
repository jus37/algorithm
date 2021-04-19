#A
A,B = map(int, input().split())
E = []
if A > B :
  for n in range(1, A+1):
    E.append(n)

  for n in range(1, B):
    E.append(-n)

  E.append(-(sum(E)))
  E = [str(n) for n in E]
  print(' '.join(E))

elif A < B:
  for n in range(1, B+1):
    E.append(-n)

  for n in range(1, A):
    E.append(n)

  E.append(-(sum(E)))
  E = [str(n) for n in E]
  print(' '.join(E))

else:
  for n in range(1, A+1):
    E.append(n)
    E.append(-n)
  E = [str(n) for n in E]
  print(' '.join(E))

#B
N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1
former = 0
for n in range(0, len(A)):
  ans *= (A[n] - former + 1)
  ans %= (10**9 + 7)
  former = A[n]

print(ans)

