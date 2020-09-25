class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def dictFromStr(s):
            letter_dict = dict()
            
            for i in range(len(s)):
                key = s[i]

                if key in letter_dict:
                    letter_dict[key] += 1
                else:
                    letter_dict[key] = 1
                    
            return letter_dict
        
        s_letters = dictFromStr(s)
        t_letters = dictFromStr(t)
        
        for key in t_letters:
            if key in s_letters:
                if t_letters[key] != s_letters[key]:
                    return key
            else:
                return key
        
        return
