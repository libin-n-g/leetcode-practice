class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies_assigned = [1] * n  # Step 1: Initialize with 1 candy per child
        # Step 2: Left-to-right pass (ensure higher-rated child gets more candies than left neighbor)
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies_assigned[i] = candies_assigned[i-1] + 1
        # Step 3: Right-to-left pass (ensure higher-rated child gets more candies than right neighbor)
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies_assigned[i] <= candies_assigned[i+1]:
                candies_assigned[i] = candies_assigned[i+1] + 1
        # Step 4: Sum up total candies
        return sum(candies_assigned)
