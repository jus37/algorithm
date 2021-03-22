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
  lis.insert(0,1)
  judge = True
  for i in range(0,len(lis)-1):
    if graph[lis[i]-1][lis[i+1]-1] == False:
      judge = False
      break
  if judge:
    ans += 1

print(ans)