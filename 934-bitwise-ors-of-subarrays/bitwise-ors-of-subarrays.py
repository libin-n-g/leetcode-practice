class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        ans_0_i = set()
        for n in arr:
            ans_0_i = { x | n for x in ans_0_i} | {n}
            result |= ans_0_i
        return len(result)