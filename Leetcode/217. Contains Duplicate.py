class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = set()

        for x in nums:
            if x in d:
                return True
            else:
                d.add(x)

        return False
