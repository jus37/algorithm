import itertools
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

lis = []
for i in itertools.permutations(range(1,N+1),N):
  lis.append(list(i))

p = lis.index(P)
q = lis.index(Q)

print(abs(p-q))