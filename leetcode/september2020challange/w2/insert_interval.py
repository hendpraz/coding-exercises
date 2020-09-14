class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low, high = newInterval[0], newInterval[1]
        
        overlaps = []
        first_overlap_idx = 0
        last_overlap_idx = 0
        
        i = 0
        for interval in intervals:
            if interval[0] > high or interval[1] < low:
                pass
            else:
                if len(overlaps) == 0:
                    first_overlap_idx = i
                    lowest = interval[0] if interval[0] < low else low
                
                overlaps.append(interval)
                last_overlap_idx = i
                highest = interval[1] if interval[1] > high else high
                
            i += 1
            
        if len(overlaps) == 0:
            if len(intervals) != 0:
                result = []
                appended = False
                for i in range(len(intervals)):
                    if intervals[i][0] > newInterval[0] and (not appended):
                        result.append(newInterval)
                        appended = True
                        
                    result.append(intervals[i])
                    
                if not appended:
                    return result + [newInterval]
                return result
            else:
                return intervals + [newInterval]
        else:
            result = []
            for i in range(first_overlap_idx):
                result.append(intervals[i])
            
            result.append([lowest, highest])
                
            for i in range(last_overlap_idx + 1, len(intervals)):
                result.append(intervals[i])
                
            return result
