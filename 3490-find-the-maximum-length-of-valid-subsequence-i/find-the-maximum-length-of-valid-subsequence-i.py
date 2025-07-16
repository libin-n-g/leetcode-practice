class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        length = {
            'odd': 0,
            'even': 0,
            'odd-even': 0,
            'even-odd': 0,
        }
        for num in nums:
            if num % 2 == 0:
                length['even'] += 1
                length['odd-even'] = length['even-odd'] + 1
            else:
                length['odd'] += 1
                length['even-odd'] = length['odd-even'] + 1
        return max(length.values())
                    