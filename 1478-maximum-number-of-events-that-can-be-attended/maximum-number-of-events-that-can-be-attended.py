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
            # skip forward current time to start of event.
            if current_day < start:
                current_day = start
            # add events starting at same current time. 
            while events and current_day == events[0][0]:
                _, end = heapq.heappop(events)
                heapq.heappush(sorted_events_by_end_time, end)
            # remove events that have end time less tan today
            while sorted_events_by_end_time and sorted_events_by_end_time[0] < current_day:
                end_time = heapq.heappop(sorted_events_by_end_time)
            # Add one event to be attented if exists.
            if sorted_events_by_end_time:
                heapq.heappop(sorted_events_by_end_time)
                attended += 1
            current_day += 1
            # No events left to pocess then proced to next starting time of events.
            if not sorted_events_by_end_time and events:
                start, end = heapq.heappop(events)
                heapq.heappush(sorted_events_by_end_time, end)

        return attended