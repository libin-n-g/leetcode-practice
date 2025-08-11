class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.minHeap = nums
        self.k = k
        while len(self.minHeap) > k:
            heappop(self.minHeap) # removes min values till k elements remain,

    def add(self, val: int) -> int:
        if len(self.minHeap) == self.k:
            heappushpop(self.minHeap, val)
        else:
            heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)