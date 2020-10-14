class RecentCounter:

    def __init__(self):
        self.requests = []
        self.last_idx = -1

    def ping(self, t: int) -> int:
        self.requests.append(t)
        if self.last_idx == -1:
            # if no valid last_idx assigned, assign the first element idx
            self.last_idx = 0
            return 1
        else:
            valid_range = range(t - 3000, t + 1)
            
            # if last_idx not in a valid_range, renew last_idx
            if self.requests[self.last_idx] not in valid_range:
                for i in range(self.last_idx, len(self.requests)):
                    if self.requests[i] in valid_range:
                        self.last_idx = i
                        break
                
            return len(self.requests) - (self.last_idx)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)