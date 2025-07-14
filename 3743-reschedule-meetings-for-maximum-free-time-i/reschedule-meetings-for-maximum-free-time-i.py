class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        i = 0
        j = -1
        total_meeting = 0
        ret = 0
        N = len(startTime)
        startTime.append(eventTime)
        endTime.append(0)
        while k > 0:
            total_meeting += endTime[i] - startTime[i]
            i += 1
            k -= 1
        while i <= N:
            ret = max(ret, startTime[i] - endTime[j] - total_meeting)
            if i < len(endTime):
                total_meeting += endTime[i] - startTime[i]            
            j += 1
            i += 1
            total_meeting -= (endTime[j] - startTime[j])
            
        return ret