'''

[A - World Cup](https://atcoder.jp/contests/abc262/tasks/abc262_a)
'''
Y = int(input())

for _ in range(100):
    if Y % 4 == 2:
        print(Y)
        exit()
    else:
        Y += 1
