'''AtCoder Beginner Contest 259'''
# [C - XX to XXX](https://atcoder.jp/contests/abc259/tasks/abc259_c)
S = input()
T = input()

i = 0
ans = 'Yes'
for c in T:
    if i < len(S) and S[i] == c:
        i += 1
    elif i > 1 and S[i-1] == S[i-2] == c:
        pass
    else:
        ans = "No"
        break
if i != len(S):
    ans = 'No'
print(ans)
