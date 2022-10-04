'''
[C - Manga ](https://atcoder.jp/contests/abc271/tasks/abc271_c)
'''
N = int(input())

a = [False] * (N + 2)

for i in map(int, input().split()):
    a[min(N + 1, i)] = True
read = 0
while N >= 0:
    read += 1
    N -= 1 if a[read] else 2
print(read - 1)
