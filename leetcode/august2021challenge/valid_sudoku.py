class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            row_set = set()
            for i in range(len(row)):
                if row[i] == ".":
                    continue
                else:
                    if row[i] in row_set:
                        return False
                    
                    row_set.add(row[i])
                    
        # check columns
        for i in range(len(board)):
            column_set = set()
            for j in range(len(board)):
                box = board[j][i]
                
                if box == ".":
                    continue
                else:
                    if box in column_set:
                        return False
                    
                    column_set.add(box)
                    
        # check 3 x 3 box
        starts = [] 
        start = (0, 0)
        
        for i in range(3):
            for j in range(3):
                starts.append(start)
                
                start = (start[0], start[1] + 3)
                
                if start[1] >= 9:
                    start = (start[0], 0)
                
            start = (start[0] + 3, start[1])
        
        for i in range(len(starts)):
            start = starts[i]
            
            box_set = set()
            
            for j in range(3):
                for k in range(3):
                    val = board[start[0] + j][start[1] + k]
                    
                    if val == ".":
                        continue
                    else:
                        if val in box_set:
                            return False
                    
                        box_set.add(val)
                    
        return True