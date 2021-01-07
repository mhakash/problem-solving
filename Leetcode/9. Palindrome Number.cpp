class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x!=0)){
          return false;
        } 
      long long revert = 0;
      long long t = x;
      while(t != 0 ){
        revert = revert * 10 + t % 10 ;
        t = t / 10;
      }
      return revert == x;
    }
};