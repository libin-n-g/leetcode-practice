class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = []
        start = 0
        for i in range(0, len(nums)):
            if nums[i] - nums[start] > k:
                result.append(nums[start:i])
                start = i
        result.append(nums[start:])
        print(result)
        return len(result)