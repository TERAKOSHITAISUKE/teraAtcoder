#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll = long long;

int main()
{
    int n, x;
    cin >> n >> x;
    vector<int> a(n), b(n);
    rep(i, n) cin >> a[i] >> b[i];
    ll ans = 2e18;
    ll s = 0, l = 1e18;
    rep(r, n)
    {
        s += a[r] + b[r];
        l = min<ll>(l, b[r]);
        if (x < r + 1)
            continue;
        ll now = s + l * (x - r - 1);
        ans = min(ans, now);
    }
    cout << ans << endl;
    return 0;
}