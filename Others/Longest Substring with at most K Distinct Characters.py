def longestSubstr(s, k):
    l = 0
    max_length = 0
    freq = {}
    curr_freq = 0
    
    for i in range(len(s)):
        r = s[i]
        f = freq.get(r, 0)
        if f == 0:
            curr_freq += 1
        freq[r] = f + 1
        
        while curr_freq > k:
            freq[s[l]] -= 1
            if freq[s[l]] == 0:
                curr_freq -= 1
            l += 1
        
        max_length = max(max_length, i - l + 1)
    
    return max_length

print(
    longestSubstr("araaci", 2)
)