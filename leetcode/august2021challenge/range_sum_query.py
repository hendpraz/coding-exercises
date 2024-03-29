class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
  
        currentTotal = 0
        for num in nums:
            currentTotal += num

            self.nums.append(currentTotal)

    def sumRange(self, left: int, right: int) -> int:
        if left >= 1:
            return self.nums[right] - self.nums[left - 1]
        else:
            return self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)