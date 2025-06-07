class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = max(gain[0], 0)
        for i in range(1, len(gain)):
            gain[i] += gain[i-1]
            max_altitude = max(max_altitude, gain[i])
        return max_altitude