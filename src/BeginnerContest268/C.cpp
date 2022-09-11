'''
[C - Chinese Restaurant](https://atcoder.jp/contests/abc268/tasks/abc268_c)
'''
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
using namespace std;
#define MOD 1000000007
#define MOD2 998244353
#define INF ((1 << 30) - 1)
#define LINF (1LL << 60)
#define EPS (1e-10)
typedef long long Int;
typedef pair<Int, Int> P;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int n;

int main()
{
    cin >> n;
    vector<int> p(n);
    rep(i, n) cin >> p[i];
    vector<int> cnt(n);
    rep(i, n)
    {
        int j = (p[i] - 1 - i - 1 + n) % n;
        rep(k, 3) cnt[(j + k) % n]++;
    }
    int and = 0;
    rep(i, n) ans = max(ans, cnt[i]);
    cout << ans << endl;
    return 0;
}
