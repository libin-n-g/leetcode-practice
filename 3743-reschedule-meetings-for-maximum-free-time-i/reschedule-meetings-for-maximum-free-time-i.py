class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Initialize free_time with the gap from time 0 to the first event's start time
        free_time = startTime[0]  
        # Variable to store the maximum free time found
        max_free_time = 0
        # Append eventTime to startTime to account for the gap after the last event
        startTime.append(eventTime)  
        # Prepend 0 to endTime to represent the start of the timeline
        endTime = [0] + endTime  
        # Get the total number of events (including eventTime)
        N = len(startTime)
        
        # Calculate the initial free time for the first k gaps
        # This includes the gap from 0 to the first event and gaps between the first k events
        for i in range(1, k):
            # Add the gap between the end of the previous event (or 0) and the start of the current event
            free_time += startTime[i] - endTime[i]
        
        # Slide a window of k events to find the maximum free time
        for i in range(k, N):
            # Add the gap between the current event's start and the previous event's end
            free_time += startTime[i] - endTime[i]
            # Update the maximum free time if the current free time is larger
            max_free_time = max(max_free_time, free_time)
            # Subtract the gap from the earliest event in the window (i-k) to slide the window
            free_time -= startTime[i - k] - endTime[i - k]
        
        # Return the maximum free time found
        return max_free_time