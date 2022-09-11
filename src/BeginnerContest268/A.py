'''
[A - Five Integers](https://atcoder.jp/contests/abc268/tasks/abc268_a)
'''
from collections import defaultdict
A, B, C, D, E = map(int, input().split())
a = [A, B, C, D, E]

dict = defaultdict(int)

for i in a:
    dict[i] += 1

sum = 0
for _ in dict:
    sum += 1
print(sum)
