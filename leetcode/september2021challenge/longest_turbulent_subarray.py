class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        elif len(arr) == 2:
            return 2 if arr[0] != arr[1] else 1
        else:
            x = arr[0]
            
            found = False
            for i in range(len(arr)):
                if x != arr[i]:
                    found = True
                    break
                    
            if not found:
                return 1
        
        maximum = 2
        current_max = 2
        
        going_up = arr[i] > arr[i-1]
        same = False
        
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[j - 1]:
                current_max = 1
                same = True
                continue
            else:
                if same:
                    going_up = arr[j] > arr[j-1]
                    same = False
                    
                    current_max = 2
                    
                elif arr[j] > arr[j - 1] and not going_up:
                    current_max += 1
                    going_up = True
                    
                elif arr[j] < arr[j - 1] and going_up:
                    current_max += 1
                    going_up = False
                    
                elif arr[j] > arr[j - 1] and going_up:
                    current_max = 2
                
                elif arr[j] < arr[j - 1] and not going_up:
                    current_max = 2
                
                maximum = max(maximum, current_max)
        
        return maximum
