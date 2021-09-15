class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        transformed_shifts = []
        
        i = len(shifts) - 1
        shift_sum = 0
        while i >= 0:
            shift_sum += shifts[i]
            shift_sum %= 26
            transformed_shifts.append(shift_sum)
            
            i -= 1
            
        # reverse
        transformed_shifts = list(reversed(transformed_shifts))
            
        otp = ""
        for i in range(len(shifts)):
            shift = transformed_shifts[i]
            
            change = (ord(s[i]) - ord('a')) + shift
            change = change % 26
            
            final_char = chr(ord('a') + change)
            otp += final_char
            
        return otp
