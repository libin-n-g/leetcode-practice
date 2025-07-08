import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        attended = 0
        sorted_events = []
        for s, e in events:
            heapq.heappush(sorted_events, [e, s])
            # current_day = max(e, current_day)
        heapq.heapify(events)
        current_day = 1
        sorted_events_by_end_time = []
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
            print(current_day, end_time)
            if end_time >= current_day:
                print(f"attended on {current_day}")
                attended += 1
            if current_day <= end_time:
                current_day += 1
            if not sorted_events_by_end_time and events:
                start, end = heapq.heappop(events)
                heapq.heappush(sorted_events_by_end_time, end)

        return attended