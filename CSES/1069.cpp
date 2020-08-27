#include<bits/stdc++.h>
using namespace std;

int main(){
  int s=1, t=1;
  string a;
  cin >> a;
  int n = a.length();
  for(int i=1; i<n; i++){
    if(a[i] == a[i-1]) {
      t++;
      s = max(s,t);
    }
    else{
      t=1;
      s = max(s,t);
    }
  }
  cout << s << '\n';
  return 0;
}