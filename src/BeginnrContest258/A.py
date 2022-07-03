
'''AtCoder Beginner Contest 258'''

'''
[A - When?](https://atcoder.jp/contests/abc258/tasks/abc258_a)
問題文
AtCoder Beginner Contest は通常、日本標準時で 21 時ちょうどに始まり 100 分間にわたって行われます。
0 以上 100 以下の整数 K が与えられます。21 時ちょうどから K 分後の時刻を HH:MM の形式で出力してください。
ただし、HH は 24 時間制での時間を、MM は分を表します。
時間または分が 1 桁のときは、先頭に 0 を追加して 2 桁の整数として表してください。

制約
K は 0 以上 100 以下の整数
'''


'''AC'''
K = int(input())
div, mod = divmod(K, 60)
if mod < 10:
    mod = "0" + str(mod)
if 0 <= div <= 2:
    h = 21 + div
    print(str(h)+":"+str(mod))
