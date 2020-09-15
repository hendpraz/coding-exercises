class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_arr = list(map(int, version1.split('.')))
        v2_arr = list(map(int, version2.split('.')))
        
        if len(v1_arr) < len(v2_arr):
            arr_tuple = (v1_arr, v2_arr, -1)
        else:
            arr_tuple = (v2_arr, v1_arr, 1)
        
        smaller_len = len(arr_tuple[0])
        bigger_len = len(arr_tuple[1])
        ret_val = arr_tuple[2]
        
        for i in range(smaller_len):
            if v1_arr[i] > v2_arr[i]:
                return 1
            elif v1_arr[i] < v2_arr[i]:
                return -1
        
        if len(v1_arr) != len(v2_arr):
            for i in range(smaller_len, bigger_len):
                if arr_tuple[1][i] > 0:
                    return ret_val
        
        return 0
        