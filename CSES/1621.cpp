#include<bits/stdc++.h>
using namespace std;

int main(){
	set<int> s;
	int n, t;
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> t;
		s.insert(t);
	}
	cout << s.size() << endl;
	return 0;
}