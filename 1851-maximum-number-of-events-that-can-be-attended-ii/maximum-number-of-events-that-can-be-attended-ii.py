from collections import defaultdict
import heapq

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time to process them in order
        events.sort()
        # Get the number of events
        n = len(events)
        # Extract start times for binary search
        starts = [s for s, _, _ in events]
        # Initialize dp array with -1 for memoization (k+1 rows for event limits, n columns for event indices)
        dp = [[-1]*n for _ in range(k+1)]
        for events_limit in range(k+1):
            for index in range(n-1, -1, -1):
                if events_limit == 0:
                    dp[0][index] = 0
                else:
                    next_start_time_index = bisect_right(starts, events[index][1])
                    # Compute max value by considering two cases:
                    # 1. Skip current event and move to next
                    # 2. Attend current event and move to next non-overlapping event
                    print(next_start_time_index)
                    dp[events_limit][index] = max(
                        0 if index == n-1 else dp[events_limit][index+1],
                        events[index][2] if next_start_time_index == n else dp[events_limit - 1][next_start_time_index] + events[index][2]  # Case 2: Including current event
                    )
        return dp[k][0]


    def maxValue_recusrsive(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time to process them in order
        events.sort()
        # Get the number of events
        n = len(events)
        # Extract start times for binary search
        starts = [s for s, _, _ in events]
        # Initialize dp array with -1 for memoization (k+1 rows for event limits, n columns for event indices)
        # Each element dp[count][cur_index] represents the maximum value that can be obtained by attending up to count events, starting from the event at index cur_index or beyond.
        dp = [[-1]*n for _ in range(k+1)]
        
        # Recursive function to compute max value with memoization
        def maxValue(index, events_limit):
            # Base case: No more events can be attended or reached end of events
            if events_limit == 0 or index == n:
                return 0
            # Return memoized result if already computed
            if dp[events_limit][index] != -1:
                return dp[events_limit][index]
            
            # Find the next event that starts after the current event ends
            next_start_time_index = bisect_right(starts, events[index][1])
            
            # Compute max value by considering two cases:
            # 1. Skip current event and move to next
            # 2. Attend current event and move to next non-overlapping event
            dp[events_limit][index] = max(
                maxValue(index+1, events_limit),  # Case 1: Not including current event
                maxValue(next_start_time_index, events_limit - 1) + events[index][2]  # Case 2: Including current event
            )
            # Return memoized result
            return dp[events_limit][index]
        
        # Start recursion from first event with k events allowed
        return maxValue(0, k)
    
    def maxValue_old(self, events: List[List[int]], k: int) -> int:
        # Create a dictionary to map start times to lists of (end_time, value) tuples
        event_start_map = defaultdict(list)
        for s, e, v in events:
            # Group events by start time for efficient processing
            event_start_map[s].append((e, v))
        
        # Initialize array to track max value achievable after attending i events (0 to k)
        best = [0] * (k + 1)
        
        # Min heap to store tuples of (end_time + 1, best_values_array)
        # Used to track best possible values up to certain end times
        min_heap = []
        
        # Process events in order of start times
        for start_time in sorted(event_start_map.keys()):
            # Remove events from heap that end before or at current start_time
            # This ensures we only consider valid, non-overlapping previous events
            while min_heap and min_heap[0][0] <= start_time:
                # Pop the earliest ending event
                end, current_best = heapq.heappop(min_heap)
                # Update best array with maximum values for each event count
                for ck in range(1, k + 1):
                    best[ck] = max(best[ck], current_best[ck])
            
            # Process all events that start at current start_time
            for end_time, value in event_start_map[start_time]:
                # Create temporary array to store best values if we include this event
                c_best = [0] * (k + 1)
                # Calculate best values for attending 1 to k events while including current event
                for ck in range(k):
                    # Add current event value to best value of previous (ck) events
                    c_best[ck + 1] = best[ck] + value
                # Push to heap with end_time + 1 to track when this event becomes available
                # for future events (can't start before this event ends)
                heapq.heappush(min_heap, (end_time + 1, c_best))
        
        # Process any remaining events in the heap
        # This handles cases where best values come from events processed later
        while min_heap:
            _, current_best = heapq.heappop(min_heap)
            # Update best array with maximum values
            for ck in range(1, k + 1):
                best[ck] = max(best[ck], current_best[ck])
        
        # Return the maximum value achievable with up to k events
        return max(best)