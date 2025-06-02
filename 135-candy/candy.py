class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies_assigned = [1]* n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies_assigned[i] = candies_assigned[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and candies_assigned[i] <= candies_assigned[i+1]:
                candies_assigned[i] = candies_assigned[i+1] + 1
        return sum(candies_assigned)
