class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occurences = dict()
        
        for num in nums:
            if num in occurences:
                occurences[num] += 1
            else:
                occurences[num] = 1
                
        results = []
        n = len(nums)
        for key in occurences:
            if occurences[key] > (n / 3):
                results.append(key)
                
        return results
