import itertools
N,M = map(int, input().split())
graph = []
for i in range(N):
  row = [False]*N
  graph.append(row)

for i in range(M):
  a,b = map(int, input().split())
  a -= 1
  b -= 1
  graph[a][b] = True
  graph[b][a] = True

lists = []
for i in itertools.permutations(range(2, N +1),N-1):
  lists.append(list(i))

ans = 0
for lis in lists:
  for i in range(0,len(lis)-1):
    if i == 0:
      if graph[0][lis[i]]:
        ans += 1
    if graph[lis[i]][lis[i+1]]:
      ans += 1

print(ans)
