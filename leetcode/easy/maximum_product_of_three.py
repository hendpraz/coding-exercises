class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ## Two Negative 1 Positive
        
        ## Three positive
        
        ## All elems are negative --
        
        ## All elems are <= 0 --
        def product_all(arr):
            temp = 1
            for el in arr:
                temp *= el
            return temp
        
        def product_three_maxes(arr):
            maxes = []
            for i in range(3):
                temp = max(arr)
                maxes.append(temp)
                arr.remove(temp)
            return product_all(maxes)
        
        def product_2min_1max(arr):
            maxes = []
            maxes.append(max(arr))
            for i in range(2):
                temp = min(arr)
                maxes.append(temp)
                arr.remove(temp)
            return product_all(maxes)
        
        max_el = max(nums)
        
        if len(nums) == 3:
            return product_all(nums)
        elif max_el == 0:
            return 0
        elif max_el < 0:
            return product_three_maxes(nums)
        else: # max_el > 0
            positive_count = 0
            for num in nums:
                if num > 0:
                    positive_count += 1
            
            if positive_count == 1: # Get 2 negative, 1 positive
                return product_2min_1max(nums)
            else: # Choose between 2 positive 1 negative or all positive
                temp1 = product_2min_1max(nums.copy())
                temp2 = product_three_maxes(nums)
                return temp1 if temp1 > temp2 else temp2
