class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_dict = dict() # pattern_dict["a"] -> "dog"
        words_dict = dict() # words_dict["dog"] -> "a"
        words = str.split()
        
        same_pattern = True
        
        if (len(pattern) != len(words)):
            same_pattern = False
        else:   
            for i in range(len(pattern)):
                word = words[i]
                current_pattern = pattern[i]
                if current_pattern in pattern_dict:    
                    if word != pattern_dict[current_pattern]:
                        same_pattern = False
                        break
                else:
                    if word in words_dict:
                        if words_dict[word] != current_pattern:
                            same_pattern = False
                            break
                    else:
                        words_dict[word] = pattern[i]

                    pattern_dict[pattern[i]] = word
                
        return (same_pattern)