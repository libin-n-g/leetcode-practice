class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        free_time = startTime[0] # gap of time b/w 0 and 1st event.
        ret = 0
        startTime.append(eventTime)  # ..... eventTime
        # # ith event end time is at position i + 1
        endTime = [0] + endTime  # 0 ......
        N = len(startTime)
        for i in range(1, k):
            # end time of previous event (or starting zero) and start time of ith event.
            # basically gaps between events
            free_time += startTime[i] -  endTime[i]
        for i in range(k, N):
            # add gap between i th event and i - 1 th event.
            free_time += startTime[i] - endTime[i]
            # print(i, i -k, total_meeting)
            ret = max(ret, free_time)
            # sutract gap between i - k th event and i -k - 1 th event. 
            free_time -= (startTime[i - k] - endTime[i - k])
        return ret