# ビット全探索問題、難しすぎるのでパス→解けた
N,M = map(int, input().split())
k = []
s = []
for _ in range(M):
  z = list(map(int, input().split()))
  k.append(z[0])
  del z[0]
  s.append(z)
p = list(map(int, input().split()))

ans = 0
for x in range(2**N):
  judge = True
  for m in range(M):
    cnt = 0
    for j in range(k[m]):
      if x & (1<<(s[m][j]-1)) > 0: #集合xに含まれているかどうか（集合xではスイッチがonになっている状態かどうか）
        cnt += 1
    if cnt % 2 != p[m]:
      judge = False
  if judge:
    ans += 1

print(ans)