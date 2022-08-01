class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        firstMax = secondMax = thirdMax = None
        
        for num in nums:
            if num == firstMax or num == secondMax or num == thirdMax:
                continue
            if firstMax is None or num > firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = num
            elif secondMax is None or num > secondMax:
                thirdMax = secondMax
                secondMax = num
            elif thirdMax is None or num > thirdMax:
                thirdMax = num
        
        if thirdMax is None or secondMax == thirdMax:
            return firstMax
        
        return thirdMax