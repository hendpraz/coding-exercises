class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        farthest = dict()
        for i in range(len(S)):
            key = S[i]
            if key in farthest:
                farthest[key] = max(i, farthest[key])
            else:
                farthest[key] = i
        
        i = 0
        results = []
        while i < len(S):
            key = S[i]
            last_idx = farthest[key]
            
            j = i + 1
            while j < last_idx:
                key = S[j]
                if farthest[key] > last_idx:
                    last_idx = farthest[key]
                j += 1
            
            
            results.append(last_idx - i + 1)
            i = last_idx + 1
            
        return results