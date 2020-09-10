import itertools

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        max_time = (23, 59)
        perms = list(itertools.permutations(A))
        pairs = []
        for perm in perms:
            pairs.append((perm[0] * 10 + perm[1], perm[2] * 10 + perm[3]))
            
        current_largest = (-1, -1)
        for pair in pairs:
            # validation
            if pair[0] <= max_time[0] and pair[1] <= max_time[1]:
                if pair[0] > current_largest[0]:
                    current_largest = pair
                elif pair[0] == current_largest[0] and pair[1] > current_largest[1]:
                    current_largest = pair

        if current_largest[0] == -1:
            return ""
        else:
            result = ""
            if (current_largest[0] < 10):
                result += "0" + str(current_largest[0])
            else:
                result += str(current_largest[0])
            
            result += ":"
            
            if (current_largest[1] < 10):
                result += "0" + str(current_largest[1])
            else:
                result += str(current_largest[1])
                
            return result
