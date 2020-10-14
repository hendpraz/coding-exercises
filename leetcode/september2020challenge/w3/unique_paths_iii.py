import copy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        path_hist = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key = "{}{}".format(i, j)
                if grid[i][j] == 0:
                    path_hist[key] = True
                else:
                    if grid[i][j] == 1:
                        i_start, j_start = i, j
                    path_hist[key] = False
        
        def validEnd(path_hist):
            for key in path_hist:
                if path_hist[key]:
                    return False
            return True
        
        def isValidCoord(i, j):
            return (i >= 0) and (j >= 0) and (i < len(self.grid)) and (j < len(self.grid[0]))
        
        def search(path_hist, path, i, j, start = False):
            key = "{}{}".format(i, j)
            if isValidCoord(i, j): 
                if path_hist[key] or start:
                    path.append(key)
                    path_hist[key] = False

                    search(path_hist, path, i, j + 1)
                    search(path_hist, path, i, j - 1)
                    search(path_hist, path, i + 1, j)
                    search(path_hist, path, i - 1, j)

                    path_hist[key] = True
                    path.pop()
                elif self.grid[i][j] == 2:
                    if validEnd(path_hist):
                        path.append(key)
                        self.result_path.append(copy.deepcopy(path))
                        path.pop()
                    
        self.result_path = []
        self.grid = grid
        
        search(path_hist, [], i_start, j_start, True)
        print(self.result_path)
        
        return len(self.result_path)
