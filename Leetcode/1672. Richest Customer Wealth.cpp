class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max = 0;
        for(auto& x: accounts){
            int t =0;
            for(auto& y: x){
                t += y;
            }
            if(t > max) max = t;
        }
        return max;
    }
};