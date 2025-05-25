class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies =  max(candies)
        ret = []
        for i in candies:
            ret.append(i + extraCandies >= max_candies)
        return ret
