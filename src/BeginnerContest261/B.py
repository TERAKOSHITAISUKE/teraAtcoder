'''
AtCoder Beginner Contest 261
[B - Tournament Result](https://atcoder.jp/contests/abc261/tasks/abc261_b)
'''
N = int(input())


def correct(a, b):
    return a+b in ["WL", "LW", "DD"]


A = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i >= j:
            continue
        if not correct(A[i][j], A[j][i]):
            print("incorrect")
            exit()

print("correct")
