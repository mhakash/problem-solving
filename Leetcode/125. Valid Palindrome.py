class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        def isAlphaneumeric(a):
            return (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9')
        
        while start < end:
            if not isAlphaneumeric(s[start]):
                start += 1
                continue
            
            if not isAlphaneumeric(s[end]):
                end -= 1
                continue
                
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True