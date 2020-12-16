class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int c = 0;
        for(int& x: nums){
           	c += x;
          	x = c;
        } 
        return nums;
    }
    
};