'''
[B - Prefix?](https://atcoder.jp/contests/abc268/tasks/abc268_b)
'''
S = input()
T = input()
if len(S) > len(T):
    print("No")
    exit()


for i, j in zip(S, T):
    if i == j:
        pass
    else:
        print("No")
        exit()

print("Yes")
