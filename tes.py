N,W = map(int, input().split())

ws = [0]
vs = [0]
for i in range(N):
  w,v = map(int, input().split())
  ws.append(w)
  vs.append(v)



value = []*N
for i in range(N+1):
  value[i].append([0]*W)

for i in range(1, N+1):
  for w in range(1, W+1):
    value[i][w] = max(value[i][w], valuse[i-1][w])
    if w - ws[i] >= 0:
      value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + va[i])

ans = max(value[N])
print(ans)

