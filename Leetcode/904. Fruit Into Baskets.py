class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        max_length = 0
        freq = {}
        curr_freq = 0
        
        for i in range(len(fruits)):
            r = fruits[i]
            f = freq.get(r, 0)
            if f == 0:
                curr_freq += 1
            freq[r] = f + 1
            
            while curr_freq > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    curr_freq -= 1
                l += 1
            
            max_length = max(max_length, i - l + 1)
    
        return max_length
