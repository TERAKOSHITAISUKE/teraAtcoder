'''
AtCoder Beginner Contest 261
[A - Intersection](https://atcoder.jp/contests/abc261/tasks/abc261_a)

'''
from collections import defaultdict
L, R, l, r = map(int, input().split())

dict = defaultdict(int)

for i in range(L, R):
    dict[i] += 1

for i in range(l, r):
    dict[i] += 1

ans = 0
for v in dict:
    if dict[v] == 2:
        ans += 1
print(ans)
