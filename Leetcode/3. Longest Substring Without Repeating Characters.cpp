#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int pos[256];
        for(int i=0; i<256; i++) pos[i] = -1;
        
        int l = s.size();
        
        int ma = 0;
        int p = 0;

        for(int i=0; i<l; i++){
		if(pos[s[i]] < p ) {
			pos[s[i]] = i;
			ma = max(ma , i - p + 1);
		}
		else {
			p = pos[s[i]] + 1;
			pos[s[i]] = i;
		}
	}
        return ma; 
    }
};

int main(){
	cout << Solution().lengthOfLongestSubstring("abcabcbb") << endl;
	return 0;
}
