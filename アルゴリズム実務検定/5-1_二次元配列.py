# ABC 157 B問題

bingo = []
for _ in range(0, 3):
  row = list(map(int, input().split()))
  bingo.append(row)

bingo_judge =[[False, False, False], [False, False, False], [False, False, False]]

N = int(input())

for _ in range(0, N):
  b = int(input())
  for i in range(0, 3):
    for j in range(0, 3):
      if bingo[i][j] == b:
        bingo_judge[i][j] = True

ans = "No"

for i in range(0, 3):
  if bingo_judge[i][0] and bingo_judge[i][1] and bingo_judge[i][2]:
    ans = "Yes"

for i in range(0, 3):
  if bingo_judge[0][i] and bingo_judge[1][i] and bingo_judge[2][i]:
    ans = "Yes"

if bingo_judge[0][0] and bingo_judge[1][1] and bingo_judge[2][2]:
  ans = "Yes"

if bingo_judge[0][2] and bingo_judge[1][1] and bingo_judge[2][0]:
  ans = "Yes"

print(ans)


# 第二回アルゴリズム検定C問題

N = int(input())

block = []

for _ in range(0, N):
  row = list(input())
  block.append(row)

for i in range(N-2, -1, -1): #3つ目の引数は順番を降順にする
  for j in range(0, 2*N-1):
    if block[i][j] != "." and (block[i+1][j-1] == "X" or block[i+1][j] == "X" or block[i+1][j+1] == "X"):
      block[i][j] = "X"

for i in range(0, N):
  print(*block[i])