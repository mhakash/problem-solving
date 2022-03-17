class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = list(map(lambda x: 1, nums))

        prefix = 1
        postfix = 1

        for i in range(len(nums) - 1):
            prefix = prefix * nums[i]
            out[i+1] = prefix

        for i in range(len(nums) - 1,  0, -1):
            postfix = postfix * nums[i]
            out[i-1] *= postfix

        return out
