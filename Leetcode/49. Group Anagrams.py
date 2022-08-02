class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            keyword = ''.join(sorted(s))
            newVal = groups.get(keyword, [])
            newVal.append(s)
            groups[keyword] = newVal 
                    
        return groups.values()