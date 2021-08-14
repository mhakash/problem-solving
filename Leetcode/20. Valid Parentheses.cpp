#include <stack>

class Solution {
    
private:
    bool isComplement(char ch1, char ch2) {
        return (
            (ch1 == '(' && (ch2 == ')')) ||
            (ch1 == '{' && (ch2 == '}')) ||
            (ch1 == '[' && (ch2 == ']')) 
          );
    }
    
    bool isOpening(char ch) {
        return (ch == '(' || ch == '{' || ch == '[');
    }
    
public:
    bool isValid(string s) {
        const int len = s.length();
        
        stack<char> t;
        
        for(int i=0; i<len; i++){
            if(t.empty()){
                t.push(s[i]);
            } else {
                const char x = t.top();
                
                if(isComplement(x, s[i])) t.pop();
                else if (isOpening(s[i])) t.push(s[i]);
                else return false;
            }
        }
        
        if(t.empty()) return true;
        return false;
    }
};