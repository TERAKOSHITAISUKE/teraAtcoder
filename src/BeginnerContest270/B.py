'''
[B - Hammer](https://atcoder.jp/contests/abc270/tasks/abc270_b)
'''
X, Y, Z = map(int, input().split())
if Y < 0:
    X, Y, Z = -X, -Y, -Z

if X < Y:
    print(abs(X))
else:
    if Z < Y:
        print(abs(Z) + abs(X-Z))
    else:
        print(-1)
