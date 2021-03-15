# 幅優先探索法の基本

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


# ABC007 C問題
from collections import deque

R, C = map(int, input().split())
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
S = []

for i in range(R):
  s = input()
  S.append(s)

sy -= 1
sx -= 1
gy -= 1
gx -= 1

dist = []
for i in range(R):
  dist.append([-1]*C)

Q = deque()
Q.append([sy, sx])
dist[sy][sx] = 0

while len(Q) >0:
  i, j = Q.popleft()

  for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
    if not (0 <= i2 < R and 0 <= j2 < C):
      continue
    if S[i][j] == "#":
      continue
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2, j2])

print(dist[gy][gx])






# 深さ優先探索法の基本

# 再起上限を増やす
import sys
sys.setrecursionlimit(1000000)

# 頂点数N, 辺情報E, 始点sは定義済みとする

visited = []
for i in range(N):
  visited.append(False)

def dfs(i):
  visited[i] = True
  for j in E[i]:
    if not visited[j]:
      dfs(j)

dfs(s)


# Atcoder Typical Contest 001
import sys
sys.setrecursionlimit(1000000)
H, W = map(int, input().split())
S = []
for i in range(H):
  s = input()
  S.append(s)

for i in range(H):
  for j in range(W):
    if S[i][j] == "s":
      si, sj = i, j
    if S[i][j] == "g":
      gi, gj = i, j

visited = []
for i in range(H):
  visited.append([False]*W)

def dfs(i, j):
  visited[i][j] = True
  for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
    if not (0 <= i2 < H and 0<= j2 < W):
      continue
    if S[i][j] == "#":
      continue
    if not visited[i2][j2]:
      dfs(i2, j2)

dfs(si, sj)

if visited[gi][gj]:
  print("Yes")
else:
  print("No")


# ABC 114 C問題

N = int(input())

ans = 0

def dfs(n, use3, use5, use7):
  global ans
  if n > N:
    return
  if use3 and use5 and use7:
    ans += 1

  dfs(10*n+3, True, use5, use7)
  dfs(10*n+5, use3, True, use7)
  dfs(10*n+7, use3, use5, True)

dfs(0, False, False, False)

print(ans)