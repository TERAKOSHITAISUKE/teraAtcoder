'''
BeginnerContest260
[B - Better Students Are Needed!](https://atcoder.jp/contests/abc260/tasks/abc260_b)
'''
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

passed = [False] * N

students = [(-A[i], i) for i in range(N)]

students.sort()

for i in range(X):
    passed[students[i][1]] = True

students = [(-B[i], i) for i in range(N) if not passed[i]]
students.sort()

for i in range(Y):
    passed[students[i][1]] = True

students = [(-(A[i] + B[i]), i) for i in range(N) if not passed[i]]
students.sort()

for i in range(Z):
    passed[students[i][1]] = True

for i in range(N):
    if passed[i]:
        print(i+1)