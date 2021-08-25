class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        
        otp = ""
        addition = 0
        
        while pointer1 >= 0 or pointer2 >= 0:
            dig1 = 0
            dig2 = 0
            
            if pointer1 >= 0:
                dig1 = int(num1[pointer1])
                
            if pointer2 >= 0:
                dig2 = int(num2[pointer2])
            
            res = dig1 + dig2 + addition
            
            addition = res // 10
            remainder = res % 10
            
            otp = str(remainder) + otp
            
            pointer1 -= 1
            pointer2 -= 1
                
        if (addition > 0):
            otp = str(addition) + otp
        
        return otp