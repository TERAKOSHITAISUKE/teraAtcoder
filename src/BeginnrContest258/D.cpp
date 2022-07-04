#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

int main()
{
    int n, q;
    cin >> n >> q;
    string s;
    cin >> s;
    int p = 0;
    rep(qi, q)
    {
        int type, x;
        cin >> type >> x;
        if (type == 1)
        {
            p = (p - x + n) % n;
        }
        else
        {
            cout << s[(p + x - 1) % n] << endl;
        }
    }
    return 0;