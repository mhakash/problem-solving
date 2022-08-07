class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uset = set()
        maxLen = 0
        left = 0
        
        for i, v in enumerate(s):
            if v in uset:
                while True:
                    if s[left] == v:
                        left += 1
                        break
                    else:
                        uset.remove(s[left])
                        left += 1
            else:
                uset.add(v)
                maxLen = max(maxLen, i - left + 1)
        
        return maxLen