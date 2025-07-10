from collections import defaultdict
import heapq

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
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
                _, current_best = heapq.heappop(min_heap)
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