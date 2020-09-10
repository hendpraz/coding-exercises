class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for num in nums:
            counter[num] = 1 if (num not in counter) else counter[num] + 1
        
        max_appearance = counter[nums[0]]
        major = nums[0]
        for key in counter:
            if counter[key] > max_appearance:
                max_appearance = counter[key]
                major = key
                
        return major