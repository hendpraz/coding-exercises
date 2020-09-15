class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(0) = nums[0]
        # f(1) = nums[1]
        # f(2) = nums[2-2] + nums[2]
        # f(3) = max(f(1), f(0)) + nums[3]
        # f(4) = max(f(2), f(1)) + nums[4]
        # So f(n) = max(f(n-2), f(n-3)) + nums[n]
        
        # final_max = max(f[n], f[n-1]) with n is max index
        def func(idx):
            if idx in self.f:
                return self.f[idx]
            else:
                if idx == 0 or idx == 1:
                    result = self.arr[idx]
                elif idx == 2:
                    result = self.arr[idx] + self.arr[idx-2]
                else:
                    result = max(func(idx-2), func(idx-3)) + self.arr[idx]
                    
                self.f[idx] = result
                return result
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            self.arr = nums
            self.f = dict()
            last_idx = len(nums) - 1

            return max(func(last_idx), func(last_idx - 1))
