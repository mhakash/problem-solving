class Solution {
    
public:
    string addBinary(string a, string b) {
        string s1, s2;
        if(a.length() > b.length()) {
            s1 = a; s2 = b;
        } else {
            s1 = b; s2 = a;
        }
        string st(s1.length() - s2.length(), '0');
        s2 = st + s2;
        
        int res = 0;
        string sum = "";
        
        for(int i = s1.length() - 1; i >= 0; i--) {
            int p1 = s1[i] - '0';
            int p2 = s2[i] - '0';
            
            int s = p1 + p2 + res;
            
            sum = s & 1 ? '1' + sum : '0' + sum;
            res = s >> 1;
            
        }
        
        if(res) sum = '1' + sum;
        return sum;
    }
};