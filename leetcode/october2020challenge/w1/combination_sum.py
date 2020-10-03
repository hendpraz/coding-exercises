from itertools import combinations_with_replacement as cwr

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def is_valid_comb(comb):
            return sum(comb) == target
        
        result = []
        min_candidates = min(candidates)
        
        i = 1
        while (min_candidates * i <= target):
            combs = cwr(candidates, i)
            for comb in combs:
                if is_valid_comb(comb):
                    result.append(list(comb))
                    
            i += 1
        
        return sorted(result, key=itemgetter(0))