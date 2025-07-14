import heapq
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # Append eventTime to startTime to account for the gap from the last event to eventTime
        startTime.append(eventTime)
        # Get the total number of events (including eventTime)
        N = len(startTime)
        # Initialize list to store time gaps; start with the gap from time 0 to the first event
        time_gaps = [(startTime[0], 0)]
        # Initialize variable to store the maximum free time found
        max_free_time = 0
        
        # Calculate time gaps between the end of one event and the start of the next
        # For index i, the gap is between endTime[i-1] and startTime[i]
        for i in range(1, N):
            time_gaps.append((startTime[i] - endTime[i-1], i))
        
        # Find the three largest time gaps using a heap
        # We select the top 3 gaps to ensure we can use a large gap even if the two gaps in the current window are already included in top 3.
        top_3_time_gaps = heapq.nlargest(3, time_gaps, key=lambda x: x[0])
        
        # Iterate through events to calculate maximum free time for each window of two consecutive gaps
        for i in range(1, N):
            # Calculate the duration of the meeting between startTime[i-1] and endTime[i-1]
            meeting_duration = endTime[i-1] - startTime[i-1]
            # Sum the gaps before and after the current event (i.e., gaps at index i and i-1)
            free_time = time_gaps[i][0] + time_gaps[i-1][0]
            # Check if any of the top 3 gaps can replace the meeting duration to increase free time
            for gap, index in top_3_time_gaps:
                # Ensure the gap is not from the current or previous event to avoid overlap
                # Also ensure the gap is at least as large as the meeting duration
                if index not in [i, i-1] and gap >= meeting_duration:
                    # Add the meeting duration to free time, effectively "moving" the meeting to the larger gap
                    free_time += meeting_duration
                    break
            # Update the maximum free time if the current free time is larger
            max_free_time = max(max_free_time, free_time)
        
        # Return the maximum free time found
        return max_free_time
# ANOTHER METHOD
# Initialize a boolean array to mark events that can be skipped
# Forward pass: Determine if each event can be skipped based on gaps before it
# Backward pass: Determine if each event can be skipped based on gaps after it
# Calculate the maximum free time by considering each event