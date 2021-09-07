class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        added = set()
        
        max_count = 0
        for i in range(len(nums)):
            num = nums[i]
            
            if num in added:
                continue
            else:
                cycle = set()
                count = 0
                while num not in cycle:
                    cycle.add(num)
                    count += 1

                    added.add(num)
                    num = nums[num]

                if count > max_count:
                    max_count = count
                
        
        return max_count
