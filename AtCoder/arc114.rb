# ARC114
# A
require 'prime'
N = gets.to_i
X = gets.split.map &:to_i

# 50までの数字のうち素数のみをprimeに格納（全部で15コ）
prime = []
Prime.each(50){|i| prime<<i}

# 上記15コの素数のうち、掛け合わせて作れるすべての値をpprimeに格納
pprime = []
1.upto(15) do |i|
  combi = prime.combination(i).to_a
  combi.each do |j|
    pprime << j.inject(:*)
  end
end
pprime.sort!

# pprimeに格納されている整数のうち、Xすべてと最小公約数が1にならない最小値がanswer
ans = 0
pprime.each do |i|
  if X.all?{|e| e.gcd(i) != 1}
    ans = i
    break
  end
end

puts ans

