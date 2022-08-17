'''
freee プログラミングコンテスト2022（AtCoder Beginner Contest 264）
[C - Matrix Reducing](https://atcoder.jp/contests/abc264/tasks/abc264_c)
'''
from itertools import product
H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for row in product((0, 1), repeat=(H1)):
    for col in product((0, 1), repeat=(W1)):
        if sum(row) != H2 or sum(col) != W2:
            continue
        c = []
        for i in range(H1):
            line = []
            for j in range(W1):
                if row[i] == 1 and col[j] == 1:
                    line.append(A[i][j])
            if line:
                c.append(line)
        if c == B:
            print('Yes')
            exit()

print('No')
