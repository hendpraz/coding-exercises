class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_can = max(candies) - extraCandies
        return [(x >= max_can) for x in candies]