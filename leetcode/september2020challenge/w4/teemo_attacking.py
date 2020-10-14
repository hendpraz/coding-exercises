class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        effect_left = 0
        total_poisoned_time = 0
        
        for i in range(len(timeSeries)):
            if i == len(timeSeries) - 1:
                total_poisoned_time += duration
            else:
                time = timeSeries[i]
                next_time = timeSeries[i + 1]
                
                j = time
                while (j < next_time) and (j < (time + duration)):
                    total_poisoned_time += 1
                    j += 1
                    
        return total_poisoned_time
