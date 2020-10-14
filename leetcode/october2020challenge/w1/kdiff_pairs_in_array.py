class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        checked = set()
        count = 0
        
        if k == 0:
            counted = set()
            
            for num in nums:
                if num in checked and num not in counted:
                    count += 1
                    counted.add(num)
                    
                checked.add(num)
        else:
            nums = set(nums)
            
            for num in nums:
                if (num + k) in checked:
                    count += 1
                    
                if (num - k) in checked:
                    count += 1
                    
                checked.add(num)
                
        return count