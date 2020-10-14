class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum = sum(gas)
        cost_sum = sum(cost)
        
        new_cost = []
        candidates = []
        
        if gas_sum >= cost_sum:
            consecutive_negative = False
            start = 0
            end = 0
            total = 0
            for i in range(len(gas)):
                diff = gas[i] - cost[i]
                
                if i == 0:
                    consecutive_negative = (diff < 0)
                    total += diff
                elif diff < 0 and consecutive_negative:
                    total += diff
                    end = i
                elif diff >= 0 and not consecutive_negative:
                    total += diff
                    end = i
                else:
                    if not consecutive_negative:
                        candidates.append(start)
                    new_cost.append((start, end, total))
                    
                    consecutive_negative = not consecutive_negative
                    start = i
                    end = i
                    total = diff
                
                if i == (len(gas) - 1):
                    if not consecutive_negative:
                        candidates.append(start)
                    new_cost.append((start, end, total))
            
            for i in candidates:
                current_balance = 0
                feasible = True
                
                for j in range(i, len(gas)):
                    current_balance += (gas[j] - cost[j])
                    
                    if current_balance < 0:
                        feasible = False
                        break
                        
                if feasible:
                    for j in range(0, i):
                        current_balance += (gas[j] - cost[j])
                        
                        if current_balance < 0:
                            feasible = False
                            break
                
                if feasible:
                    return i
            

        else:
            return -1
