class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        last = nums[0]
        i = 1
        while(i < len(nums)):
            if nums[i] == last:
                while i < len(nums) and nums[i] == last:
                    nums.pop(i)
                    
            if i < len(nums) and nums[i] != last:
                last = nums[i]
            i += 1
        
        return len(nums)