#include<bits/stdc++.h>
using namespace std;

int main(){
  long long n, s=0, t;
  cin >> n;
  for(int i=0; i<n-1; i++){
    cin >> t;
    s += t;
  }

  cout << n*(n+1)/2 - s <<'\n';
}