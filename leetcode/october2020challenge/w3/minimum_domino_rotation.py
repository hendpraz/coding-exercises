class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        counter = [0] * 7
        for i in range(len(A)):
            counter[A[i]] += 1
            
            if B[i] != A[i]:
                counter[B[i]] += 1
                
        feasible = False
        feasibleNum = []
        for i in range(1, 6 + 1):
            if counter[i] == len(A):
                feasible = True
                feasibleNum.append(i)
                
        if feasible:
            minMove = len(A) + 1
            
            for num in feasibleNum:
                aMove = 0
                bMove = 0
                for i in range(len(A)):
                    if A[i] != num:
                        aMove += 1
                    
                    if B[i] != num:
                        bMove += 1
                        
                minMove = min(min(aMove, bMove), minMove)
                
            return minMove
        else:
            return -1
