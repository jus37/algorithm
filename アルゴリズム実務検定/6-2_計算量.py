# 第一回アルゴリズム実技検定 H問題
# TREにならない解法

N = int(input())
C = list(map(int, input().split()))
Q = int(input())
# 合計販売枚数
sell = 0
# セット販売で支払うカード枚数(sは奇数の場合のみ)
z = 0
s = 0

min_s_C = 1000000000
min_z_C = 1000000000

# セット販売対象の最小値とそれ以外の最小値を記録
for i in range(0, N):
  if i % 2 == 0: #本来はカード番号奇数がセット販売対象だが、配列は0からなので偶数へずれてしまう
    # i%2==0のうち、最小の数値を変数として取得
    min_s_C = min(C[i], min_s_C)
  else:
    # i%2==1のうち、最小の数値を変数として取得
    min_z_C = min(C[i], min_z_C)

# クエリの実行
for _ in range(0, Q):
  query = list(map(int, input().split()))
# 単品販売はカード在庫があることを確認した後に実際に在庫を減らす
  if query[0] == 1:
    x = query[1] - 1  # 対象となるカード番号
    a = query[2]  # 減らす枚数

    if x % 2 == 0: #カード番号が奇数（配列内では偶数）であれば
      card_x = C[x] - z - s #セット販売と全種類販売数をマイナスした枚数が現在の在庫
    else:
      card_x = C[x] - z

    if card_x >= a:
      C[x] -= a
      sell += a

      # カード在庫を直接変更したため、カード移動の処理の後、最小を更新
      if x % 2 == 0:
        min_s_C = min(C[x], min_s_C)
      else:
        min_z_C = min(C[x], min_z_C)
# セット販売、全種類販売は最小値の在庫が足りることを確認した後に、合計販売枚数のみ記録
  elif query[0] == 2:
    a = query[1]
    if min_s_C - s - z >= a:
      s += a

  elif query[0] == 3:
    a = query[1]
    if min(min_s_C - s - z, min_z_C - z) >= a:
      z += a

# 最後にセット販売・全種類販売の合計販売枚数を算出
for i in range(0, N):
  if i % 2 == 0:
    sell += s

sell += z * N

print(sell)


# 参考（TREになる解法）

N = int(input())
C = list(map(int, input().split()))
Q = int(input())

sell = 0

for _ in range(0, Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    x = query[1] - 1
    a = query[2]

    if C[x] >= a:
      C[x] -= a
      sell += a

  elif query[0] == 2:
    a = query[1]

    ok = True

    for i in range(0, N):
      if i % 2 == 0:
        if C[i] < a:
          ok = False

    if ok:
      for i in range(0,N):
        if i % 2 == 0:
          C[i] -= a
          sell += a

  elif query[0] == 3:
    a = query[1]

    ok = True

    for i in range(0, N):
      if C[1] < a:
        ok = False

    if ok:
      for i in range(0, N):
        C[i] -= a
        sell += a

print(sell)
