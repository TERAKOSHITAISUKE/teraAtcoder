'''
001 - Yokan Party
(https://atcoder.jp/contests/typical90/tasks/typical90_a)
'''
N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]


def ok(l: int):
    left_idx = 0
    for _ in range(K+1):
        right_idx = left_idx
        while(right_idx < len(A) and A[right_idx] - A[left_idx] < l):
            right_idx += 1
        if right_idx == len(A):
            return False
        left_idx = right_idx
    return True


bottom, top = 1, L+1

while top - bottom > 1:
    mid = (top + bottom) // 2
    if ok(mid):
        bottom = mid
    else:
        top = mid

print(bottom)
