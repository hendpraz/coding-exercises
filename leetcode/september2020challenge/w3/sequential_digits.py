class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_depth = 0
        temp_low = low
        while temp_low > 0:
            low_depth += 1
            temp_low //= 10
            
        high_depth = 0
        temp_high = high
        while temp_high > 0:
            high_depth += 1
            temp_high //= 10
            
        results = []
        for depth in range(low_depth, high_depth + 1):
            for i in range(1, 10 - depth + 1):
                k = i
                res = 0
                for j in range(depth):
                    res = (res*10) + k
                    k += 1
                
                if res >= low and res <= high:
                    results.append(res)
        
        return results
