class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ZERO_ROWS = 2 ** 32
        ZERO_COLS = 2 ** 32 + 1
        ZERO_ROWS_COLS = 2 ** 32 + 2
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if matrix[i][0] == ZERO_ROWS_COLS:
                        pass
                    elif matrix[i][0] == ZERO_COLS:
                        matrix[i][0] = ZERO_ROWS_COLS
                    else:
                        matrix[i][0] = ZERO_ROWS
                        
                    if matrix[0][j] == ZERO_ROWS_COLS:
                        pass
                    elif matrix[0][j] == ZERO_ROWS:
                        matrix[0][j] = ZERO_ROWS_COLS
                    else:
                        matrix[0][j] = ZERO_COLS
                    

        
        for i in range(1, len(matrix)):
            if matrix[i][0] == ZERO_ROWS:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
                    
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == ZERO_COLS:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
                    
        if matrix[0][0] == ZERO_ROWS_COLS:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
        for i in range(0, 1):
            if matrix[i][0] == ZERO_ROWS:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
                    
        for i in range(0, 1):
            if matrix[0][i] == ZERO_COLS:
                for j in range(len(matrix)):
                    matrix[j][i] = 0