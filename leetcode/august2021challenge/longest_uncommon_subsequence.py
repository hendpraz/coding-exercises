class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s1, s):
            s2 = s
            
            if len(s1) > len(s2):
                return False
            elif len(s1) == len(s2):
                return s1 == s2
            else:
                for i in range(len(s1)):
                    idx = s2.find(s1[i])
                    
                    if idx == -1:
                        return False
                    else:
                        s2 = s2[idx+1:]
                
                return True
        
        is_unsub = [True] * len(strs)
        
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    is_unsub[i] = False
                    break
                
        longest = -1
        for i in range(len(is_unsub)):
            if is_unsub[i]:
                if len(strs[i]) > longest:
                    longest = len(strs[i])
                
        return longest
