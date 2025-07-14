import heapq
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.append(eventTime)
        endTime = [0] + endTime
        meeting_duration = 0
        N = len(endTime)
        time_gaps = []
        max_free_time = 0
        for i in range(N):
            time_gaps.append((startTime[i] - endTime[i], i))
        top_3 = heapq.nlargest(3, time_gaps, key=lambda x: x[0])
        print(top_3)
        for i in range(1, N):
            meeting_duration = endTime[i] - startTime[i - 1]
            free_time = time_gaps[i][0] + time_gaps[i-1][0]
            for gap, index in top_3:
                if index not in [i, i-1] and gap >= meeting_duration:
                    free_time += meeting_duration
                    break
            max_free_time = max(max_free_time, free_time)

        return max_free_time

