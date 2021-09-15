class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        chars = dict()
        
        # init dict
        for i in range(ord('a'), ord('z') + 1):
            chars[chr(i)] = 0
        
        # add 1st char
        chars[keysPressed[0]] = releaseTimes[0]
        
        # check for next characters
        for i in range(1, len(keysPressed)):
            key = keysPressed[i]
            duration = releaseTimes[i] - releaseTimes[i - 1]
            
            if chars[key] < duration:
                chars[key] = duration
        
        # find char with longest duration and also lexicographically larger
        longest_char = keysPressed[0]
        longest_duration = releaseTimes[0]
        
        for key in chars:
            if chars[key] >= longest_duration:
                longest_char = key
                longest_duration = chars[key]
                
        return longest_char
