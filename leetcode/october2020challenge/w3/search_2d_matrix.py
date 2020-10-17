class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(matrix, target, i, j, m, n):
            # print(i, j)
            if j >= n or i >= m:
                return False
            elif matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                return False
            elif j + 1 >= n or i + 1 >= m:
                # if already on the edge, check any feasible way
                # if no feasible way, return False
                if j + 1 < n:
                    return search(matrix, target, i, j + 1, m, n)
                
                if i + 1 < m:
                    return search(matrix, target, i + 1, j, m, n)
                
                # no way
                return False
            else:
                # check downway first, then check rightway
                # if no feasible way, return False
                if matrix[i + 1][j] <= target:
                    return search(matrix, target, i + 1, j, m, n)
                elif matrix[i][j + 1] <= target:
                    return search(matrix, target, i, j + 1, m, n)
                else:
                    return False
        
        if len(matrix) == 0:
            return False
        else:
            return search(matrix, target, 0, 0, len(matrix), len(matrix[0]))
