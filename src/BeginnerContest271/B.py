'''
[B - Maintain Multiple Sequences](https://atcoder.jp/contests/abc271/tasks/abc271_b)
'''
N, Q = map(int, input().split())
L = list([(int, input().split())] for _ in range(N))
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1

    print(L[s][0][1][t])
