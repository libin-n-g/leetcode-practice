class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        i = 0
        j = -1
        total_meeting = 0
        ret = 0
        N = len(startTime)
        while k > 0:
            total_meeting += endTime[i] - startTime[i]
            i += 1
            k -= 1
        while i <= N:
            right_time_limit = eventTime if i == N else startTime[i]
            left_time_limit = 0 if j == -1  else endTime[j]
            ret = max(ret, right_time_limit - left_time_limit - total_meeting)
            # print(left_time_limit, right_time_limit, total_meeting)
            if i < len(endTime):
                total_meeting += endTime[i] - startTime[i]            
            j += 1
            i += 1
            left_time_limit = endTime[j]
            total_meeting -= (endTime[j] - startTime[j])
            
        return ret