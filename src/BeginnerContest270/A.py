'''
[A - 1-2-4 Test](https://atcoder.jp/contests/abc270/tasks/abc270_a)
'''
from collections import defaultdict

dict = defaultdict(int)

A, B = map(int, input().split())

if A == 1 or A == 2 or A == 4:
    dict[A] += 1
elif A == 3:
    dict[1] += 1
    dict[2] += 1
elif A == 5:
    dict[1] += 1
    dict[4] += 1
elif A == 6:
    dict[2] += 1
    dict[4] += 1
elif A == 7:
    dict[1] += 1
    dict[2] += 1
    dict[4] += 1
else:
    pass

if B == 1 or B == 2 or B == 4:
    dict[B] += 1
elif B == 3:
    dict[1] += 1
    dict[2] += 1
elif B == 5:
    dict[1] += 1
    dict[4] += 1
elif B == 6:
    dict[2] += 1
    dict[4] += 1
elif B == 7:
    dict[1] += 1
    dict[2] += 1
    dict[4] += 1
else:
    pass

sum = 0
for i in dict:
    sum += i

print(sum)
