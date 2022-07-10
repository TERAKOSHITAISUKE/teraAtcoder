'''AtCoder Beginner Contest 259'''
# [A - Growth Record](https://atcoder.jp/contests/abc259/tasks/abc259_a)
N, M, X, T, D = map(int, input().split())

high = D*X
born = T - high
ans = 0
if X <= M:
    ans = born + X * D
    print(ans)
else:
    ans = born + M * D
    print(ans)
