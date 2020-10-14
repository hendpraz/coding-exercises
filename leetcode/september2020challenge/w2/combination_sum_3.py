import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        perms = itertools.combinations([i for i in range(1, 10)], k)
        perms = list(perms)
        
        result = []
        for perm in perms:
            sum_perm = sum(perm)
            if sum_perm == n:
                result.append(list(perm))
        
        return result
