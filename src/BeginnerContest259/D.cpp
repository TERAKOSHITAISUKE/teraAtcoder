#include <bits/stdc++.h>
using namespace std;
#include <ac-library/atcoder/all>
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;

struct V
{
    ll x, y;
    V(ll x = 0, ll y = 0) : x(x), y(y) {}
};

int main()
{
    int n;
    cin >> n;
    V s, t;
    cin >> s.x >> s.y;
    cin >> t.x >> t.y;
    vector<V> o(n);
    vector<ll> r(n);
    rep(i, n)
    {
        cin >> o[i].x >> o[i].y >> r[i];
    };
    auto pow2 = [](ll x)
    { return x * x; };
    auto dist = [&](V a, V b)
    {
        return pow2(a.x - b.x) + pow2(a.y - b.y);
    };
    int si = 0, ti = 0;
    rep(i, n)
    {
        if (dist(s, o[i]) == pow2(r[i]))
            si = i;
        if (dist(s, o[i]) == pow2(r[i]))
            ti = i;
    };

    dsu uf(n);
    rep(i, n) rep(j, i)
    {
        ll d = dist(o[i], o[j]);
        ll r1 = r[i], r2 = r[j];
        if (r1 > r2)
            swap(r1, r2);
        if (d > pow2(r1 + r2))
            continue;
        if (d > pow2(r2 - r1))
            continue;
        uf.merge(i, j);
    };

    if (uf.same(si, ti))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}