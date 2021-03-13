# Frog1(Atcoder Educational DP Contest) A
# 動的計画法を用いた解法
N = int(input())
h = list(map(int, input().split()))

cost = [0]*N

cost[0] = 0
cost[1] = cost[0] + abs(h[0]-h[1])

for i in range(2, N):
  cost[i] = min(cost[i-1] + abs(h[i-1]-h[i]), cost[i-2] + abs(h[i-2]-h[i]))

print(cost[N-1])


# メモ化再帰関数で実装
import sys
sys.setrecursionlimit(100000)

N = int(input())
h = list(map(int, input().split()))

cost = [0] * N

done = [False]*N

def rec(i):
  if done[i]:
    return cost[i]
  if i == 0:
    cost[i] = 0
  elif i == 1:
    cost[i] = rec(0) + abs(h[0]-h[1])
  else:
    cost[i] = min(rec(i-1) + abs(h[i-1]-h[i]), rec(i-2) + abs(h[i-2] - h[i]))

  done[i] = True
  return cost[i]

print(rec(N-1))

# Frog1(Atcoder Educational DP Contest) B
N,K = map(int, input().split())
h = list(map(int, input().split()))

cost = [0]*N
cost[0] = 0

for i in range(1, N):
  costs = []
  for j in range(1, K+1):
    if i < j:
      break
    else:
      costs.append(cost[i-j] + abs(h[i]-h[i-j]))
  cost[i] = min(costs)

print(cost[N-1])


# 第三回 アルゴリズム実技検定 H問題
N,L = map(int, input().split())
h = list(map(int, input().split()))
T1,T2,T3 = map(int, input().split())

H = [False]*(L+1)
for i in h:
  h[i] = True

cost = [10**100]*(L+1)
cost[0] = 0

for i in range(1, L+1):
  cost[i] = min(cost[i], cost[i-1] + T1)
  if i >= 2:
    cost[i] = min(cost[i], cost[i-2] + T1 + T2)
  if i >= 4:
    cost[i] = min(cost[i], cost[i-4] + T1 + T2*3)
  if h[i]:
    cost[i] += T3

ans = cost[L]
for i in [L-3, L-2, L-1]:
  if i >= 0:
    ans = min(ans, cost[i] + T1//T2 + T2*(2*(L-i)-1)//2)

print(ans)


# Knapsack1(AtCoder Educational DP Contest D問題)
N,W = map(int, input().split())

ws = [0]
vs = [0]

for i in range(N):
  w,v = list(map(int, input().split()))
  ws.append(w)
  vs.append(v)

# 品物iまで受取状況完了している際に、各重さ0~Wまでの価値の最大値を二重配列として獲得
value = []
for i in range(N+1):
  value.append([-10**18]*(W+1))

value[0][0] = 0

for i in range(1, N+1):
  for w in range(W+1):
    # 品物iを受け取らない場合
    value[i][w] = max(value[i][w], value[i-1][w])
    # 品物iを受け取る場合
    if w-ws[i] >= 0:
      value[i][w] = max(value[i][w], value[i-1][w-ws[i]] + vs[i])

ans = max(value[N])
print(ans)

