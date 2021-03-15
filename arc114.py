N = int(input())
X = list(map(int, input().split()))
X.sort()
judge = [True]*N
S =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = 1

for s in S:
  judge_2 = True
  if s in X:
    ans *= s
    judge_2 = False
  for x in range(0, N):
    if X[x] % s == 0 and judge[x]:
      if judge_2:
        ans *= s
        s = 1
      judge[x] = False


print(ans)

N = int(input())
X = list(map(int, input().split()))
X.sort()
judge = [True]*N
S =[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
ans = 1

for s in S:
  cnt = 0
  for x in range(0, N):
    if X[x]%s==0 and judge[x]:
      cnt += 1
      judge[x] = False
  if cnt > 0:
    ans *= s
print(ans)
