class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelMap = {}
        for jewel in jewels:
            jewelMap[jewel] = True
        
        jewelCount = 0
        
        for stone in stones:
            if stone in jewelMap:
                jewelCount += 1
        
        return jewelCount