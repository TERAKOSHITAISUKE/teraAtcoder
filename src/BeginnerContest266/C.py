'''
[C - Convex Quadrilateral](https://atcoder.jp/contests/abc266/tasks/abc266_c)
'''


def ccw(p1, p2, p3):
    p1[0] -= p2[0]
    p3[0] -= p2[0]
    p1[1] -= p2[1]
    p3[1] -= p2[1]
    return p1[0] * p3[1] - p3[0] * p1[1] < 0


P = []
for _ in range(4):
    P.append(list(map(int, input().split())))
for i in range(4):
    if not ccw(P[i][:], P[(i+1) % 4][:], P[(i+2) % 4][:]):
        print('No')
        exit()
print('Yes')
