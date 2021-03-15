# A
A,B = gets.split.map &:to_i

if A+B >= 15 && B >= 8
  puts 1
elsif A+B >= 10 && B >= 3
  puts 2
elsif A+B >= 3
  puts 3
else
  puts 4
end


# B
N = gets.to_i

a = []
b = []

N.times do
  ai, bi = gets.split.map &:to_i
  a << ai
  b << bi
end

a_min = a.min
b_min = b.min
a_pos = a.index(a_min)
b_pos = b.index(b_min)

if a_pos == b_pos
  a.delete_at(a_pos)
  b.delete_at(b_pos)
  a_min2 = a.min
  b_min2 = b.min
  if a_min + b_min <= a_min2 && a_min + b_min <= b_min2
    puts a_min + b_min
  elsif a_min2 > b_min2
    puts [b_min2, a_min].max
  elsif
    puts [a_min2, b_min].max
  end
else
  puts [a_min, b_min].max
end


# C
N = gets.to_i
ary = gets.split.map &:to_i
ans = 0

for i in (-200..199)
  for j in (i+1..200)
    ans += (i - j)**2 * ary.count(i) * ary.count(j)
  end
end

puts ans