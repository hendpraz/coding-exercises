class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        set_size = len(nums)
        pow_set_size = pow(2, set_size)
        
        otp = []
        otp_set = set()
        for counter in range(pow_set_size):
            res = []
            key = ""
            for j in range(set_size):
                if((counter & (1 << j)) > 0):
                    res.append(nums[j])
                    key += str(nums[j]) + "."
                    
            if key not in otp_set:
                otp_set.add(key)
                otp.append(res)
        
        return otp