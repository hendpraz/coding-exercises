class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x = num1.split('+')
        y = num2.split('+')
        
        # first num
        real1 = int(x[0])
        img1 = x[1]
        
        x = img1.split('i')
        coef1 = int(x[0])
        
        # second num
        real2 = int(y[0])
        img2 = y[1]
        
        y = img2.split('i')
        coef2 = int(y[0])
        
        # process multiplication
        real_mul = real1 * real2
        img_mul = coef1 * coef2 * (-1)
        
        img_res = coef1 * real2 + coef2 * real1
        
        # form result string
        result = str(real_mul+img_mul) + "+" + str(img_res) + "i"
        
        return result
