'''AtCoder Beginner Contest 258'''

'''
[D - Trophy](https://atcoder.jp/contests/abc258/tasks/abc258_d)
問題文
問題文
N 個のステージからなるゲームがあり、i(1≤i≤N) 番目のステージは A i分間のストーリー映像と Bi分間のゲームプレイによって構成されます。
初めて i 番目のステージをクリアするためにはストーリー映像の視聴とゲームプレイを両方行う必要がありますが、二回目以降はストーリー映像をスキップすることができるので、ゲームプレイのみでクリアすることができます。
初めから遊べるのは 1 番目のステージのみですが、i(1≤i≤N−1) 番目のステージをクリアすることにより、i+1 番目のステージも遊べるようになります。
合計 X 回ステージをクリアするために必要な時間の最小値を求めてください。ただし、同じステージを複数回クリアしたとしても、全てクリア回数に数えられます。

制約
- 1≤N≤2×10**5
- 1≤Ai,Bi≤10**9
- (1≤i≤N)
- 1≤X≤10**9
- 入力は全て整数
'''


'''かつっぱさんAC'''
N, X = map(int, input().split())
A = []
B = []
Bmin = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    Bmin.append(b)

for i in range(1, N):
    A[i] += A[i-1]
    B[i] += B[i-1]
    Bmin[i] = min(Bmin[i], Bmin[i-1])

ans = 10 ** 20
for i in range(N):
    tmp = A[i] + B[i] + Bmin[i] * max(0, (X-(i+1)))
    ans = min(ans, tmp)

print(ans)
