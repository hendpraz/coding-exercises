class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # easiest solution:
        new_nums = []
        
        for i in range(len(nums) - k, len(nums)):
            new_nums.append(nums[i])
            
        for i in range(len(nums) - k):
            new_nums.append(nums[i])
            
        for i in range(len(nums)):
            nums[i] = new_nums[i]
