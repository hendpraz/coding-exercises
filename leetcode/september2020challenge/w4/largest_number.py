class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def removeLeadingZeros(string):
            last_zero = -1
            for i in range(len(string)):
                if string[i] == '0':
                    last_zero = i
                else:
                    break
                    
            if last_zero == -1:
                return string
            elif last_zero == len(string) - 1:
                return "0"
            else:
                return string[last_zero + 1:]
            
        def getMaximum(candidates_idx, str_nums):
            def sameCandidates(candidates_idx, str_nums):
                # print("running sameCandidates: ", candidates_idx)
                anchor = str_nums[candidates_idx[0]]
                for idx in candidates_idx:
                    str_num = str_nums[idx]
                    if str_num != anchor:
                        return False
                    
                return True
            
            def handleInsufficientLength(candidates_idx, str_nums, digit_loc):
                def isTailBiggerEqualHead(head, str_num, digit_loc):
                    tail = str_num[digit_loc:]
                    # print("TRYING: ", str_num)
                    
                    # print("HEAD", head)
                    while len(tail) != 0:
                        head_tail = tail[:digit_loc]
                        # print("HEAD_TAIL", head_tail)
                        
                        if len(head_tail) < len(head):
                            # compare each char
                            head_tail += head
                            for i in range(len(head)):
                                # print("FINAL COMPARE OF {}, HEAD: {}, HEAD_TAIL: {}".format(str_num, head, head_tail))
                                if head_tail[i] < head[i]:                         
                                    # print("FAILED at LAST: ", str_num)
                                    return False
                                elif head_tail[i] > head[i]:
                                    # print("SURVIVED1: ", str_num)
                                    return True
                                elif i >= len(tail):
                                    # print("SURVIVED2: ", str_num)
                                    return True
                                
                                # print("WHAT THE... ", str_num)
                        elif head_tail < head:
                            # print("FAILED EARLY: ", str_num)
                            return False
                        elif head_tail > head:
                            # print("SURVIVED3: ", str_num)
                            return True
                        
                        tail = tail[digit_loc:]
                    
                    # print("SURVIVED4: ", str_num)
                    return True
                
                first_candidate_num = str_nums[candidates_idx[0]]
                head = first_candidate_num[:digit_loc]
                
                # print("Insufficient! Candidates_idx: ", candidates_idx, "STR: ", str_nums)
                # print("Head: ", head)
                
                remained_exist = False
                i = 0
                while i < len(candidates_idx):
                    idx = candidates_idx[i]
                    str_num = str_nums[idx]
                    
                    if isTailBiggerEqualHead(head, str_num, digit_loc):
                        # The candidate remain
                        if len(str_num) > len(head):
                            remained_exist = True
                        i += 1
                    else:
                        # The candidate popped
                        popped = candidates_idx.pop(i)
                
                if remained_exist:
                    i = 0
                    while i < len(candidates_idx):
                        idx = candidates_idx[i]
                        str_num = str_nums[idx]
                        
                        if len(str_num) == len(head):
                            popped = candidates_idx.pop(i)
                        else:
                            i += 1
                    
                return candidates_idx
            
            # print("First Candidates:" ,candidates_idx)
            digit_loc = 0
            while not sameCandidates(candidates_idx, str_nums):
                greatest_prefix = '0'
                insufficient_length = False
                for i in range(len(candidates_idx)):
                    idx = candidates_idx[i]
                    str_num = str_nums[idx]
                    
                    if digit_loc > len(str_num) - 1:
                        insufficient_length = True
                    elif str_num[digit_loc] > greatest_prefix:
                        greatest_prefix = str_num[digit_loc]
                        
                # print("Greates_prefix: ", greatest_prefix)
                # print("Digit loc: ", digit_loc)
                
                i = 0
                while i < len(candidates_idx):
                    idx = candidates_idx[i]
                    str_num = str_nums[idx]
                    
                    if insufficient_length:
                        candidates_idx = handleInsufficientLength(candidates_idx, str_nums, digit_loc)
                        insufficient_length = False
                    else:
                        if digit_loc > len(str_num) - 1:
                            i += 1
                        elif str_num[digit_loc] < greatest_prefix:
                            popped = candidates_idx.pop(i)
                            # print("Popping candidate:", popped)
                        else:
                            i += 1
                            
                digit_loc += 1
            
            # print("Final Candidates:" ,candidates_idx)
            return candidates_idx
        
        str_nums = []
        
        for num in nums:
            str_nums.append(str(num))
            
        result = ""
        
        while len(str_nums) != 0:
            candidates_idx = []
            
            greatest_prefix = '0'
            for str_num in str_nums:
                if str_num[0] > greatest_prefix:
                    greatest_prefix = str_num[0]
                    
            for i in range(len(str_nums)):
                if str_nums[i][0] >= greatest_prefix:
                    candidates_idx.append(i)
                    
            chosen_candidates_idx = getMaximum(candidates_idx, str_nums)
            
            popped = 0
            for idx in chosen_candidates_idx:
                num = str_nums.pop(idx - popped)
                # print(num)
                result += num
                popped += 1
        
        return removeLeadingZeros(result)
