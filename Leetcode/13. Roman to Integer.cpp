#include <map>
class Solution {
public:
    int romanToInt(string s) {
        std::map<char,int> roman;
        
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;
        
        int l = s.length();
        
        int r = 0;
        for(int i=0; i<l-1; i++){
            if(roman[s[i]] >= roman[s[i+1]]) r += roman[s[i]];
            else r -= roman[s[i]];
        }
        r += roman[s[l-1]];
        
        return r;
    }
};