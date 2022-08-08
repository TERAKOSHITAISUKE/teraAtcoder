'''
[C - Monotonically Increasing](https://atcoder.jp/contests/abc263/tasks/abc263_c)
'''
from itertools import combinations
N, M = map(int, input().split())
A = [i+1 for i in range(M)]

for i in combinations(A, N):
    print(*i)
