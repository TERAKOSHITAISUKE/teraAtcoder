'''AtCoder Beginner Contest 259'''
# [B - Counterclockwise Rotation](https://atcoder.jp/contests/abc259/tasks/abc259_b)
import numpy as np
a, b, d = map(int, input().split())


radi = np.deg2rad(d)
cosX = np.cos(radi)
sinX = np.sin(radi)

x = (a*cosX) - (b*sinX)
y = (a*sinX) + (b*cosX)

print(x, y)
