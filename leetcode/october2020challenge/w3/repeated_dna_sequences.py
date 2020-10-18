class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:        
        if len(s) <= 10:
            return []
        
        patterns = dict()
        for i in range(len(s) - 9):
            chunk = s[i:i + 10]
            if chunk in patterns:
                patterns[chunk] += 1
            else:
                patterns[chunk] = 1
        
        result = []
        for key in patterns.keys():
            if patterns[key] > 1:
                result.append(key)
        
        return result
