class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = [(nums[i] if (i % 2 == 0) else nums[i+n]) for i in range(n)]
        return new_nums