
'''AtCoder Beginner Contest 258'''

'''
B - [Number Box](https://atcoder.jp/contests/abc258/tasks/abc258_b)
問題文
正整数 N が与えられます。
N 行 N 列のマス目があり、上から i 行目、左から j 列目のマスには数字 A i,jが書かれています。
このマス目は上下および左右がつながっているものとします。つまり以下が全て成り立ちます。
(1,i) の上のマスは (N,i) であり、(N,i) の下のマスは (1,i) である。(1≤i≤N)
(i,1) の左のマスは (i,N) であり、(i,N) の右のマスは (i,1) である。(1≤i≤N)
高橋君は、上下左右および斜めの 8 方向のうちいずれかを初めに選びます。
そして、好きなマスから決めた方向に 1 マス移動することを N−1 回繰り返します。
高橋君は N 個のマス上を移動することになりますが、
高橋君が通ったマスに書かれている数字を左から通った順番に並べた整数としてあり得る最大のものを求めてください。

制約
- 1≤N≤10
- 1≤Ai,j≤9
入力はすべて整数。
'''


'''かつっぱさんAC'''
N = int(input())
A = [input() for _ in range(N)]
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1, 1, 1, 0, -1, 1, 0, -1]

ans = "0"

for i in range(N):
    for j in range(N):
        for d in range(8):
            num = ""
            for k in range(N):
                x = (i + dx[d]*k) % N
                y = (j + dy[d]*k) % N
                num += A[x][y]
            ans = max(ans, num)

print(ans)
