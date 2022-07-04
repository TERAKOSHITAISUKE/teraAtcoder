'''AtCoder Beginner Contest 258'''

'''
[C - Rotation](https://atcoder.jp/contests/abc258/tasks/abc258_c)
問題文
正整数 N,Q と、長さ N の英小文字からなる文字列 S が与えられます。
以下で説明されるクエリを Q 個処理してください。クエリは次の 2 種類のいずれかです。
1 x: 「S の末尾の文字を削除し、先頭に挿入する」という操作を x 回連続で行う。
2 x: S の x 番目の文字を出力する。
制約
- 2≤N≤5×10**5
- 1≤Q≤5×10**5
- 1≤x≤N
- ∣S∣=N
- S は英小文字からなる。
- 2 x の形式のクエリが 1 個以上与えられる。
- N,Q,x はすべて整数。
'''


'''AC'''
N, Q = map(int, input().split())
S = input()

s = 0

for _ in range(Q):
    num, el = map(int, input().split())
    if num == 1:
        s = (s - el) % N
    if num == 2:
        print(S[(s + el - 1) % N])
