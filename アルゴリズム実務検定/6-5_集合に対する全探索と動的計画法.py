# 第一回アルゴリズム実技検定 G問題
N = int(input())
A = []
for i in range(N-1):
  lst = list(map(int, input().split()))
  A.append([0]*(i+1) + lst) #すべてNつの要素にするため

ALL = 1 << N #=2**N

happy = [0]*ALL
# 該当する1〜Nの数字(i)が集合に含まれているかを確認
def has_bit(n, i):
  return (n & (1<<i) > 0)

# すべての集合の組み合わせにおける幸福度の算出
# ありえる集合パターンを2進数で表記し、それに対してi,jが含まれているかをhas_bitで確認
for n in range(ALL):
  for i in range(N):
    for j in range(i+1, N):
      if has_bit(n, i) and has_bit(n, j):
        happy[n] += A[i][j]

ans = -10**100

for n1 in range(ALL):
  for n2 in range(ALL):
    if n1&n2 > 0: #集合にかぶりがあったらアウト
      continue
    n3 = ALL-1 - (n1|n2)
    ans = max(ans, happy[n1] + happy[n2] +happy[n3])

print(ans)