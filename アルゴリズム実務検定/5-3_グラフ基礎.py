# 第三回 アルゴリズム実技検定 E問題
  # 隣接行列
N, M, Q = map(int, input().split())

graph = []
for i in range(0, N):
  row = [False]*N
  graph.append(row)

for i in rage(0, M):
  u, v = map(int, input().split())

  u -= 1
  v -= 1

  graph[u][v] = True
  graph[v][u] = True

C = list(map(int, input().split()))

for i in range(0, Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    x = query[1]
    x -= 1

    print(C[x])

    for i in range(0, N):
      if graph[x][i]:
        C[i] = C[x]

  if query[0] == 2:
    x = query[1]
    y = query[2]
    x -= 1
    print(C[x])
    C[x] = y

# 隣接リスト
N, M, Q = map(int, input().split())

graph = []
for i in range(0, N):
  row = []
  graph.append(row)

for i in range(0, M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1

  graph[u].append(v)
  graph[v].append(u)

C = list(map(int, input().split()))

for i in range(0, Q):
  query  = list(map(int, input().split()))

  if query[0] == 1:
    x = query[1]
    x -= 1

    print(C[x])

    for i in graph[x]:
      C[i] = C[x]

  if query[0] == 1:
    x = query[1]
    y = query[2]
    x -= 1

    print(C[x])
    C[x] = y


# 第一回 アルゴリズム実技検定 E問題

N, Q = map(int, input().split())

status = []
for _ in range(0, N):
  row = []
  for _ in range(0, N):
    row.append("N")
  status.append(row)

for _ in range(0, Q):
  log, user = map(int, input().split())
  if log == 1:
    status[user[0]-1][user[1]-1] = "Y"

  elif log == 2:
    for i in range(0, N):
      if status[i][user-1] == "Y":
        status[user-1][i] = "Y"

  elif log == 3:
    to_follow = []
    for i in range(0, N):
      if status[user-1][i] == "Y":
        for j in range(0, N):
          if status[i][j] == "Y" and j != user-1:
            to_follow.append(j)
    for k in to_follow:
      status[user-1][k] = "Y"

for i in range(0, N):
  print(*status[i])