N = gets.to_i
count = []
dainaris = []
shounaris = []
N.times do
  a = gets.split(" ")
  if a.include?(">")
    dainaris << a[1].to_i
  elsif a.include?("<")
    shounaris << a[1].to_i
  else
    count << a[1].to_i
  end
end
dainari = dainaris.max
shounari = shounaris.min

for i in ((dainari+1)..(shounari-1))
    judge = true
    for w in count
        if i % w != 0
            judge =false
        end
    end
    if judge
        puts i
        exit
    end
end
ans = []
(M-N+1).times do |n|
  sum = 0
  N.times do |j|
    sum += ames[n+j]
  end
  ans << sum
end
