class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int t=1;
        for(int i=1; i<nums.size(); i++){
            if(nums[i] != nums[i-1]) {
                t++;
                nums[t-1] = nums[i];
            }
        }
        
        return t;
    }
};