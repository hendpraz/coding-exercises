class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ending_here = 1
        min_ending_here = 1
        
        max_so_far = 1
        positive_exist = False
        consecutive_negative = False
        
        for i in range(len(nums)):
            if nums[i] > 0:
                max_ending_here *= nums[i]
                min_ending_here = min(min_ending_here * nums[i], 1)
                positive_exist = True
            elif nums[i] == 0:
                max_ending_here = 1
                min_ending_here = 1
            else: # nums[i] < 0
                if min_ending_here < 0:
                    consecutive_negative = True
                temp = max_ending_here
                max_ending_here = max(min_ending_here * nums[i], 1)
                min_ending_here = temp * nums[i]
                
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
                
        if len(nums) == 1:
            return nums[0]
        elif (not positive_exist) and (not consecutive_negative) and (max_so_far == 1):
            return 0
        else:
            return max_so_far
