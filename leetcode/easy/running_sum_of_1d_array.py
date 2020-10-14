class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        temp_arr = []
        for x in nums:
            temp_arr.append(x + temp)
            temp += x
        
        return temp_arr