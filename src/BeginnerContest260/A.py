'''
BeginnerContest260
https://atcoder.jp/contests/abc260

[A - A Unique Letter](https://atcoder.jp/contests/abc260/tasks/abc260_a)
'''
from collections import defaultdict
S = input()
dict = defaultdict(int)

for _ in S:
    dict[_] += 1

for i in dict:
    if dict[i] == 1:      
        print(i)
        exit()

print(-1)