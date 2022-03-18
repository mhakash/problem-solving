class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = curr_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sum + nums[i] > nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum
