# A
a,b = map(int, input().split())
c,d = map(int, input().split())
print(b-c)

# B
x =list(input())
if "." in x:
  del x[x.index("."):len(x)]
x = "".join(x)
print(x)

# C
N = int(input())
n = len(str(N))
ans = 0
for i in range(1,n):
  if i % 2 == 0:
    ans += 9*(10**(i//2-1))

if n % 2 == 0:
  ans += N //(10**(n//2)) - (10**(n//2-1))
  if N // 10**(n//2) <= N % 10**(n//2):
    ans += 1

print(ans)

# D
