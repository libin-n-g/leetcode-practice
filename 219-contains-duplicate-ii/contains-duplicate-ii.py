class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexer = {}
        for i, n in enumerate(nums):
            # can be made with set too.
            if n in indexer and i - indexer[n] <= k:
                return True
            indexer[n] = i
        return False
            