N = int(input())
count = []
dainaris = []
shounaris = []
for _ in range(N):
  a = list(input().split())
  if ">" in a:
    dainaris.append(int(a[1]))
  elif "<" in a:
    shounaris.append(int(a[1]))
  else:
    count.append(int(a[1]))

dainari = max(dainaris)
shounari = min(shounaris)

for i in range(dainari+1, shounari):
  judge = True
  for w in count:
    if i % w != 0:
      judge = False
  if judge:
    print(i)
