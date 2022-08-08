'''
[B - Ancestor](https://atcoder.jp/contests/abc263/tasks/abc263_b)
'''
N = int(input())
P = [0, 0] + list(map(int, input().split()))

cnt = 0
while N != 1:
    N = P[N]
    cnt += 1

print(cnt)
