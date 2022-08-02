class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        n = len(nums)
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        countNum = [None] * (n + 1)

        for key in freqMap:
            index = freqMap[key]
            if countNum[index] is None:
                countNum[index] = []
            countNum[index].append(key)

        topK = []

        for i in range(n, -1, -1):
            if countNum[i]:
                for num in countNum[i]:
                    topK.append(num)
                    k -= 1
                    if k == 0:
                        return topK
            