class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ans_set = set()
        n = len(nums)
        for i in range(n):
            # starting from i
            divisible_count = 0
            sub_array = ""
            for j in range(i, n):
                sub_array += str(nums[j]) + "_"
                if nums[j] % p == 0:
                    divisible_count += 1
                if divisible_count <= k:
                    ans_set.add(sub_array)
                else:
                    break
        return len(ans_set)
        