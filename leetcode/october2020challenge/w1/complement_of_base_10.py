class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        x = 1
        while x <= N:
            x *= 2
            
        x -= 1
        
        return x ^ N
