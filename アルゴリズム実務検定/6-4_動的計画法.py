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

done = [False}*N

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


# 動的計画法なし
N = int(input())
ary = list(map(int, input().split()))

now = 0
ans = 0

while now < N-1:
  if now != N-2:
    step1 = abs(ary[now+1]-ary[now])
    step2 = abs(ary[now+2]-ary[now])
    if step1 >= step2:
      ans += step2
      now += 2
    else:
      ans += step1
      now += 1
  else:
    ans += abs(ary[now+1]-ary[now])
    now += 1

print(ans)

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