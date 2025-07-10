import heapq
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        event_start_map = defaultdict(list)
        for s, e, v in events:
            event_start_map[s].append((e, v))
        # tracks the best value after we attended kth event.
        best = [0]*(k+1)
        min_heap = []

        for start_time in sorted(event_start_map.keys()):
            # Loop to find best one till now
            while min_heap and min_heap[0][0] <= start_time:
                _, current_best = heapq.heappop(min_heap)
                for ck in range(1, k+1):
                    best[ck] = max(best[ck], current_best[ck])

            # Loop to get total value if we add an event from starting from current start_time
            for end_time, value in event_start_map[start_time]:
                c_best = [0] *(k+1)
                for ck in range(k):
                    # current best is what was best in previous timepoint + current value
                    # note that we have to add one to event number as we are adding an event
                    c_best[ck + 1] = best[ck] + value
                # Tracks best possibel values for cbest array as end_time + 1 instant. 
                # Note that we are doing end_time+1 as we need to use it 
                # when we get start_t,ime == end_time + 1 to find best possible best array
                heapq.heappush(min_heap, (end_time + 1, c_best))
        while min_heap:
            _, current_best = heapq.heappop(min_heap)
            for ck in range(1, k+1):
                best[ck] = max(best[ck], current_best[ck])
        return max(best)