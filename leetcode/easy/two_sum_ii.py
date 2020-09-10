class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = dict()
        
        for i in range(len(numbers)):
            if target - numbers[i] in num_dict:
                return [num_dict[target - numbers[i]] + 1] + [i + 1]
            else:
                num_dict[numbers[i]] = i
            
        return