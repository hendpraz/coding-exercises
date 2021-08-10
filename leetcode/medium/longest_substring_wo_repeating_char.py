class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        current_max = 0
        for i in range(len(s)):
            j = i
            exist_set = set()
            count = 0
            
            while j < len(s) and s[j] not in exist_set:
                exist_set.add(s[j])
                count += 1
                j += 1
                
            current_max = max(current_max, count)
            
        return current_max