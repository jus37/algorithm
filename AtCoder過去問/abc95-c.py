A,B,C,X,Y = map(int, input().split())
ans = 10**100
cnt = max(X, Y)
for i in reversed(range(0, cnt+1)):
  money = 0
  money += i * 2*C
  if X > i:
    money += A*(X-i)
  if Y > i:
    money += B*(Y-i)
  ans = min(ans,money)
print(ans)