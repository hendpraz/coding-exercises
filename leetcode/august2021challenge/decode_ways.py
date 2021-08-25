class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        if len(s) == 1:
            return 1
        
        last_num = "9"
        # find leading zeros, separate zeros
        for i in range(len(s)):
            ch = s[i]
            
            if ch == "0":
                if last_num == "1" or last_num == "2":
                    continue
                else:
                    return 0
                
            last_num = ch
            
        count1 = 1
        count2 = 1
        
        for i in range(1, len(s)):
            ch = s[i]
            last_ch = s[i-1]
            
            d = int(ch) - int('0')
            dd = (int(last_ch) - int('0')) * 10 + d
            
            count = 0
            
            if d > 0:
                count += count2
                
            if dd >= 10 and dd <= 26:
                count += count1
                
            count1 = count2
            count2 = count
            
        return count2