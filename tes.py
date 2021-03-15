from collections import deque

# 頂点数N, 辺情報E, 始点sは定義済みとする

visited = []
for i in range(N):
  visited.append(False)

Q = deque()
Q.append(s)
visited[s] = True

while len(Q) > 0:
  i = Q.popleft()
  for j in E[i]:
    if not visited[j]:
      visited[j] = True
      Q.append(j)

from collections import deque

R,C = map(int, input().split())
h = []
judge = []
for i in range(0, R):
  h.append([-1]*C)
  judge.append([True]*C)


sy,sx = map(int, input().split())
gy,gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1

map = []
for _ in range(R):
  x = input()
  map.append(x)

Q = deque()
Q.append([sy,sx])
judge[sy][sx] = True
while len(Q) > 0:
  y,x = Q.popleft()
  for i,j in [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]:
    if map[i][j] == "." and i>= 0 and j >= 0 and judge[i][j]:
      h[i][j] = h[y][x] + 1
      judge[i][j] = False
      Q.append([i,j])

print(h[gy][gx])

