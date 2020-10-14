class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = dict()
        for num in nums:
            counter[num] = 1 if num not in counter else counter[num] + 1
            
        total = 0
        for key in counter:
            val = counter[key] - 1
            if val > 0:
                total += (val * (val + 1)) // 2
            
        return total