class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import math
        needed = {}
        for x in t:
            needed[x] = needed.get(x,0) + 1
        
        needCount = len(needed)
        
        has = {}
        hasCount = 0
        
        i, j = 0, 0
        currMin = float('infinity')
        
        l = 0
        
        for r in range(len(s)):
            has[s[r]] = has.get(s[r], 0) + 1
            if s[r] in needed and has[s[r]] == needed[s[r]]:
                hasCount += 1
            
            while hasCount == needCount:
                if (r - l + 1) < currMin:
                    currMin = r - l + 1
                    i = l
                    j = r
                
                if s[l] in needed:
                    if has[s[l]] == needed[s[l]]:
                        hasCount -= 1
                    has[s[l]] = has[s[l]] - 1
                
                l += 1
        
        if math.isinf(currMin):
            return ""
        
        return s[i:j+1]
                    
                    