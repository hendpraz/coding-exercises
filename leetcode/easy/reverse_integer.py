class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT_STR = "2147483647"
        MIN_INT_STR = "2147483648"
        
        is_negative = (x < 0)
        
        # check if x can be reversed
        s = str(abs(x))
        s = s[::-1]
        
        if len(s) > len(MAX_INT_STR):
            return 0
        elif len(s) == len(MAX_INT_STR):
            found = False
            for i in range(len(s)):
                if not found:
                    if is_negative:
                        if s[i] > MIN_INT_STR[i]:
                            return 0
                        elif s[i] < MIN_INT_STR[i]:
                            found = True
                    else:
                        if s[i] > MAX_INT_STR[i]:
                            return 0
                        elif s[i] < MAX_INT_STR[i]:
                            found = True
                else:
                    break
                    
        return int(s) * -1 if is_negative else int(s)