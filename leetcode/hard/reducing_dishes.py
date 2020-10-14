class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        def getScore(arr):
            total = 0
            for i in range(len(arr)):
                total += arr[i] * (i + 1)
                
            return total
        
        sorted_arr = sorted(satisfaction)
        
        max_sum = 0
        
        for i in range(len(sorted_arr)):
            score = getScore(sorted_arr[i:])
            max_sum = max(max_sum, score)
            
        return max_sum