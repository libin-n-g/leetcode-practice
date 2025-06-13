class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        sorted_nums = sorted(nums)
        N = len(sorted_nums)
        def check(max_limit):
            i = 1
            pair_count = 0
            while i < N:
                if abs(sorted_nums[i] - sorted_nums[i-1]) > max_limit:
                    i+=1
                else:
                    i+=2
                    pair_count += 1
                    if pair_count == p:
                        return True
            return pair_count >= p
        right = 10**9
        left = 0
        while left < right:
            mid = left + (right - left)//2
            if check(mid):
                right = mid 
            else:
                left = mid + 1
        return left