class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        i = 0
        j = -1
        total_meeting = 0
        ret = 0
        N = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)
        for i in range(k):
            total_meeting += endTime[i] - startTime[i]
        i = k
        for i in range(k, N+1):
            ret = max(ret, startTime[i] - endTime[i - k - 1] - total_meeting)
            if i < len(endTime):
                total_meeting += endTime[i] - startTime[i]
            total_meeting -= (endTime[i - k] - startTime[i - k])
            
        return ret