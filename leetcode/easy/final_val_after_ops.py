class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        total = 0
        for op in operations:
            if op[1] == "+":
                total += 1
            else:
                total -= 1
                
        return total
