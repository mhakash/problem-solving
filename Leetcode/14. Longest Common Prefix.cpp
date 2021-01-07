class Solution {
  
    int commonPrefixSize(string& x, string& y){
      int l = min(x.length(), y.length());
      int s = 0;
      for(int i=0; i<l; i++){
        if(x[i] == y[i]) s++;
        else break;
      }
      return s;
    }
  
public:
    
    string longestCommonPrefix(vector<string>& strs) {
      int l = strs.size();
      if(l == 0) return "";
      if(l == 1) return strs[0];
      int lcp = commonPrefixSize(strs[0], strs[1]);
      for(int i=1; i<l-1; i++){
        lcp = min(commonPrefixSize(strs[i], strs[i+1]), lcp);
      }
      return strs[0].substr(0,lcp);
    }
  
};