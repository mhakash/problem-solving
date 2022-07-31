class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        hi = False
        size = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                if not hi:
                    hi = True
                size += 1

            elif hi and s[i] == ' ':
                break

        return size
