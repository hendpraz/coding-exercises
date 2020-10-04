class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        remaining = len(intervals)
        
        for i in range(len(intervals)):
            lower = intervals[i][0]
            higher = intervals[i][1]
            
            for j in range(len(intervals)):
                if i == j:
                    continue
                    
                interval = intervals[j]

                if interval[0] <= lower and interval[1] >= higher:
                    remaining -= 1
                    break
                    
        return remaining
