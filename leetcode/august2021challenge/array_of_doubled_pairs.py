class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        num_dict = dict()
        sorted_arr = sorted(arr)
        
        positive_arr = []
        negative_arr = []
        
        zero_count = 0
        
        for num in arr:
            if num > 0:
                positive_arr.append(num)
            elif num < 0:
                negative_arr.append(num)
            else:
                zero_count += 1
                
        if zero_count % 2 != 0:
            return False
        
        positive_arr = sorted(positive_arr)
        negative_arr = sorted(negative_arr, reverse=True)
        
        all_arr = positive_arr + negative_arr
        
        all_dict = dict()
        
        for num in all_arr:
            if num not in all_dict:
                all_dict[num] = 0

            all_dict[num] += 1

        for num in all_dict:
            if all_dict[num] > 0:
                if (num * 2) not in all_dict:
                    return False
                
                remainder = all_dict[num * 2] - all_dict[num]
                
                if remainder < 0:
                    return False
                else:
                    all_dict[num] = 0
                    all_dict[num * 2] = remainder
        
        return True
        
        