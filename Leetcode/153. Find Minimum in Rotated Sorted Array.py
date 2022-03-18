class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while r - l > 1:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m
            else:
                r = m

        return min(nums[l], nums[r])
