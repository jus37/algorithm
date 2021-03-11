# ABC 46 A問題
  # 全探索
N = int(input())

cnt = 0
n = 0

while cnt != N:
  n += 1
  m = set(list(str(n))) #重複した要素を消す
  if len(m) == 1:
    cnt += 1

print(n)

# 数学的解法
# 各桁ゾロ目は9種類しかないことからN番目のゾロ目を解く
import math
N = int(input())
# N // 9 + 1だと割り切れるときに1多くなってしまう
x = math.ceil(N / 9) #x の「天井」 (x 以上の最小の整数) を返す

y = N % 9
if y == 0:
  y = 9

ans = ""

for _ in range(0, x):
  ans += str(y)

print(ans)


# 第二回 アルゴリズム実技検定 D問題
def is_match(T, S):
  for i in range(0, len(S) - len(T) + 1):
    ok = True

    for j in range(0, len(T)):
      if S[i + j] != T[j] and T[j] != ".":
        ok = False

    if ok:
      return True

  return False

S = input()

C = "abcdefghijklmnopqrstuvwxyz."

M = []

for T in C:
  if is_match(T, S):
    M.append(T)

for c1 in C:
  for c2 in C:
    T = c1 + c2
    if is_match(T, S):
      M.append(T)

for c1 in C:
  for c2 in C:
    for c3 in C:
      T = c1 + c2 + c3
      if is_match(T, S):
        M.append(T)

print(len(M))
