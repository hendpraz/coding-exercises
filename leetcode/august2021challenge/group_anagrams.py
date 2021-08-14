class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()
        
        for s in strs:
            key = str(sorted(s))
            
            if key not in str_dict:
                str_dict[key] = [s]
            else:
                str_dict[key].append(s)
                
        otp = []
        for key in str_dict:
            otp.append(str_dict[key])
            
        return otp