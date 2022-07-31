'''AtCoder Beginner Contest261
[C - NewFolder(1)](https://atcoder.jp/contests/abc261/tasks/abc261_c)
'''
from collections import defaultdict
N = int(input())

dict = defaultdict(int)

for _ in range(N):
    S = input()
    if dict[S] == 0:
        print(S)
    else:
        print(S + "(" + str(dict[S]) + ")")
    dict[S] += 1
