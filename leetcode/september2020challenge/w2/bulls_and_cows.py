class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        
        secret_map = list(map(str, secret))
        guess_map = list(map(str, guess))
        
        i = 0
        max_i = len(secret)
        while i < max_i:
            if secret_map[i] == guess_map[i]:
                bull += 1
                secret_map.pop(i)
                guess_map.pop(i)
                max_i -= 1
            else:
                i += 1
                
        secret_dict = {}
        for i in range(len(secret_map)):
            key = secret_map[i]
            if key in secret_dict:
                secret_dict[key] += 1
            else:
                secret_dict[key] = 1
        
        for i in range(len(guess_map)):
            key = guess_map[i]
            if key in secret_dict:
                secret_dict[key] -= 1
                if secret_dict[key] >= 0:
                    cow += 1
                    
        return "{}A{}B".format(bull, cow)
