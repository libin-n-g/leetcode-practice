class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        start = nums[0]
        for n in nums[1:]:
            if n - start > k:
                count +=1
                start = n
        count+=1
        return count