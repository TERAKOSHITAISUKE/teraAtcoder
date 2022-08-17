'''
freee プログラミングコンテスト2022（AtCoder Beginner Contest 264）
[B - Nice Grid](https://atcoder.jp/contests/abc264/tasks/abc264_b)
'''
grid = ("###############",
        "#.............#",
        "#.###########.#",
        "#.#.........#.#",
        "#.#.#######.#.#",
        "#.#.#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.#.#.#.#.#.#.#",
        "#.#.#.###.#.#.#",
        "#.#.#.....#.#.#",
        "#.#.#######.#.#",
        "#.#.........#.#",
        "#.###########.#",
        "#.............#",
        "###############")

R, C = map(int, input().split())
R -= 1
C -= 1
if grid[R][C] == '#':
    print('black')
else:
    print('white')