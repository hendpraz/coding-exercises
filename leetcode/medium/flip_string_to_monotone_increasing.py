class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        costs = []
        
        i = 0
        while i < len(s):
            if s[i] == "1":
                start = i
                end = i
                cost = 0
                zero_found = False
                
                while i < len(s):
                    if s[i] == "0":
                        cost += 1
                        zero_found = True
                        
                    elif s[i] == "1":
                        if zero_found:
                            i -= 1
                            break
                        else:
                            end = i
                        
                    i += 1
                    
                if zero_found == False:
                    break
                
                one_to_zero = end - start + 1
                zero_to_one = cost
                
                costs.append( [one_to_zero, zero_to_one, 0] )            
            i += 1
        
        if len(costs) == 0:
            return 0
        elif len(costs) == 1:
            ret = min(costs[0][0], costs[0][1])
            return ret
        
        i = len(costs) - 1
        my_sum = 0
        
        while i >= 0:
            my_sum += costs[i][1]
            
            costs[i][2] = my_sum
            
            i -= 1
            
        print(costs)
        
        current_min = costs[0][2]
        
        flip_ones_before = costs[0][0]
        flip_zeros_before = costs[0][1]
        
        for i in range(1, len(costs)):
            cost_el = costs[i]
            addition = min(flip_ones_before, flip_zeros_before)
            
            current_min = min(current_min, cost_el[2] + addition)
            
            flip_ones_before += cost_el[0]
            flip_zeros_before += cost_el[1]
            
        return min(current_min, flip_ones_before)