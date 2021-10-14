#include<iostream>
using namespace std;

#define ll long long

int main() {
    int t;

    cin >> t;

    while(t--) {
        ll x, y;
        cin >> y >> x;
        
        if(y <= x){
            if(x & 1) cout << x * x - y + 1 << '\n';
            else cout << (x - 1) * (x - 1) + y << '\n';
        } else {
            if (y & 1) cout << (y - 1) * (y - 1) + x << '\n';
            else cout << y * y - x + 1 << '\n';
        }
    }

    return 0;
}