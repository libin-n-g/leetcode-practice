class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        N = len(nums)
        bit_map = defaultdict(int)
        max_or = 0
        result = []
        for i, num in enumerate(nums[::-1]):
            max_or |= num
            pos = 0
            while num > 0:
                if num % 2 == 1:
                    bit_map[pos] = N - i - 1
                pos+=1
                num = num >> 1
            # print(nums[-i-1], bit_map)
            if bit_map:
                result.append(max(bit_map.values())  - N + i + 1 + 1)
            else:
                result.append(1)
        return result[::-1]