'''
002 - Encyclopedia of Parentheses
https://atcoder.jp/contests/typical90/tasks/typical90_b
'''
from itertools import combinations
N = int(input())

if N % 2 != 0:
    exit()


def to_parenthes(opens):
    chars = [')'] * N
    for open_pos in opens:
        chars[open_pos] = '('
    return ''.join(chars)


for opens in combinations(list(range(N)), N//2):
    parenthes = to_parenthes(opens)
    cnt = 0
    ok = True
    for c in parenthes:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            ok = False
    if ok:
        print(parenthes)
