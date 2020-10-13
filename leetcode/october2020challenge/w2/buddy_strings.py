class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == 1:
            return False
        else:
            a_disposition = []
            
            for i in range(len(A)):
                if A[i] != B[i]:
                    a_disposition.append((A[i], B[i]))
            
            if len(a_disposition) == 0:
                # check if same element exist
                a_set = set()
                for letter in A:
                    if letter in a_set:
                        return True
                    else:
                        a_set.add(letter)
                        
                return False
            elif len(a_disposition) == 2:
                if a_disposition[0][0] == a_disposition[1][1] and a_disposition[0][1] == a_disposition[1][0]:
                    return True
                else:
                    return False
            else:
                return False