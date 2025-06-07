class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ret = [0]*(len(gain) + 1)
        for i in range(len(gain)):
            ret[i+1] = ret[i] + gain[i]
        return max(ret)