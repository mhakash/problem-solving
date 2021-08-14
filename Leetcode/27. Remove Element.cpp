#include<algorithm>

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        
        for(int i=0; i<nums.size(); i++) {
            if(nums[i] == val) count++;
        }
        
        for(int i = 0 ; i < nums.size(); i++) {
            if(nums[i] == val) {
                for(int j = nums.size() - count; j < nums.size(); j++){
                    if(nums[j] != val) {
                        swap(nums[i], nums[j]);
                        break;
                    }
                }
            }
        }
        
        return nums.size() - count;
    }
};