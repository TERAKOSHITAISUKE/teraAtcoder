'''
[D - Left Right Operation ](https://atcoder.jp/contests/abc263/tasks/abc263_d)
'''
N, L, R = map(int, input().split())
A = list(map(int, input().split()))

accumulate = [0]

for element in A:
    accumulate.append(accumulate[-1] + element)

left = [l * L - accumulate[l] for l in range(N+1)]
right = [(N-r)*R + accumulate[r] for r in range(N+1)]

rightmin = right
for i in range(N-1, -1, -1):
    rightmin[i] = min(rightmin[i], rightmin[i+1])

ans = L * N

for l in range(N):
    tmp = left[l] + rightmin[l]
    ans = min(ans, tmp)

print(ans)
