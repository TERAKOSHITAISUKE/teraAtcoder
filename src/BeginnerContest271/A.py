'''
[A - 484558](https://atcoder.jp/contests/abc271/tasks/abc271_a)
'''
N = int(input())
n = hex(N)[2:]
if len(n) == 1:
    print('0' + n.upper())
else:
    print(n.upper())
