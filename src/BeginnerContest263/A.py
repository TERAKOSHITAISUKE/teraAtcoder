'''
[A - Full House](https://atcoder.jp/contests/abc263/tasks/abc263_a)
'''
A, B, C, D, E = map(int, input().split())

dict = [0] * 14

dict[A] += 1
dict[B] += 1
dict[C] += 1
dict[D] += 1
dict[E] += 1

ans = []
for d in dict:
    if d != 0:
        ans.append(d)

if ans == [2, 3] or ans == [3, 2]:
    print("Yes")
else:
    print("No")
