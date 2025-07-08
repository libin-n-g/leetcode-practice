import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        attended = 0
        current_day = 1
        heapq.heapify(events)
        sorted_events_by_end_time = []
        # Add first item to start loop
        start, end = heapq.heappop(events)
        heapq.heappush(sorted_events_by_end_time, end)
        while sorted_events_by_end_time:
            # skip forward to current time
            if current_day < start:
                current_day = start
            # add events starting at same starting time. 
            while events and current_day == events[0][0]:
                start, end = heapq.heappop(events)
                heapq.heappush(sorted_events_by_end_time, end)
            end_time = heapq.heappop(sorted_events_by_end_time)
            if end_time >= current_day:
                attended += 1
            if current_day <= end_time:
                current_day += 1
            if not sorted_events_by_end_time and events:
                start, end = heapq.heappop(events)
                heapq.heappush(sorted_events_by_end_time, end)

        return attended