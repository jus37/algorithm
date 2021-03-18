S = input()
ans = 0
result = 0
for i in range(len(S)):
  if S[i] == "A" or S[i] == "T" or S[i] == "C" or S[i] == "G":
    result += 1
    ans = max(ans,result)
  else:
    result = 0

print(ans)