#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using P = pair<int, int>;

vector<bool> ok;

int main()
{
    int n, x, y, z;
    cin >> n >> x >> y >> z;
    vector<int> a(n), b(n);
    rep(i, n) cin >> a[i];
    rep(i, n) cin >> b[i];
    ok = vector<bool>(n);

    vector<P> p;
    rep(i, n) p.emplace_back(-a[i], i);
    sort(p.begin(), p.end());
    rep(i, x) ok[p[i].second] = true;

    p = vector<P>();
    rep(i, n) if (!ok[i])
    {
        p.emplace_back(-b[i], i);
    }
    sort(p.begin(), p.end());
    rep(i, y) ok[p[i].second] = true;

    p = vector<P>();
    rep(i, n) if (!ok[i])
    {
        p.emplace_back(-a[i] - b[i], i);
    }
    sort(p.begin(), p.end());
    rep(i, z) ok[p[i].second] = true;

    rep(i, n) if (ok[i]) cout << i + 1 << endl;
    return 0;
}