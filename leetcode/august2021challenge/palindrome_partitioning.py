class Solution:
    def minCut(self, s: str) -> int:
        cut = [0 for i in range(len(s))]
        palindrome = [[False for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)):
            minCut = i
            for j in range(i + 1):
                if (s[i] == s[j] and (i - j < 2 or palindrome[j + 1][i - 1])):      
                    palindrome[j][i] = True
                    minCut = min(minCut,0 if  j == 0 else (cut[j - 1] + 1))
                    
            cut[i] = minCut
        return cut[len(s) - 1]