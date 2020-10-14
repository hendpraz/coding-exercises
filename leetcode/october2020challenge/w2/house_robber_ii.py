class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(0) = nums[0]
        # f(1) = nums[1]
        # f(2) = nums[2-2] + nums[2] (if we dont pick last element)
        # f(2) = nums[2] (if we pick last element)
        # f(3) = max(f(1), f(0)) + nums[3]
        # f(4) = max(f(2), f(1)) + nums[4]
        # So f(n) = max(f(n-2), f(n-3)) + nums[n]
        
        # But if we choose f(n), we cannot choose f(0)
        
        # final_max = max(f[n], f[n-1]) with n is max index
        def func(idx, last):
            # check if value exist in dictionary
            if last:
                if idx == 0:
                    return 0
                elif idx in self.f_last:
                    return self.f_last[idx]
            else:
                if idx in self.f_exclude_last:
                    return self.f_exclude_last[idx]
                
            # calculate result
            if idx == 0 or idx == 1:
                result = self.arr[idx]
            elif idx == 2:
                result = self.arr[idx]
                if not last:
                    result += self.arr[idx-2] # idx 0
            else:
                result = max(func(idx-2, last), func(idx-3, last)) + self.arr[idx]
    
            # assign to dictionary
            if last:
                self.f_last[idx] = result
            else:
                self.f_exclude_last[idx] = result
            
            return result

        def seed():
            for i in range(len(self.arr)):
                res = func(i)
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            self.arr = nums
            self.f_last = dict()
            self.f_exclude_last = dict()
            last_idx = len(nums) - 1
            
            # seed()
            include_last = func(last_idx, True)
            include_2nd_last = func(last_idx - 1, False)
            exclude_last_two = func(last_idx - 2, False)
            
            print(include_last, include_2nd_last, exclude_last_two)
            return max(max(include_last, include_2nd_last), exclude_last_two)
