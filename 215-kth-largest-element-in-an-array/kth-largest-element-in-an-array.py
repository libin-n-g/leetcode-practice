class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for item in nums:
            heappush(heap, -item)
        for i in range(k):
            item = heappop(heap)
        return -item