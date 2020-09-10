class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def getNumberFactors(num):
            factors = []
            for i in range(1, num // 2 + 1):
                if num % i == 0:
                    factors.append(i)
            
            return factors
        
        factors = getNumberFactors(len(s))
        
        found = False
        for factor in factors:
            if found:
                break
            pattern = s[:factor]
            found = True
            
            temp = s
            while len(temp) != 0:
                head, temp = temp[:factor], temp[factor:]
                if len(temp) == 0:
                    if head == pattern:
                        found = True
                    else:
                        found = False
                elif head != pattern:
                    found = False
                    break
        
        return found