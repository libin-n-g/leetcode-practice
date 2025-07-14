import heapq
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # Append eventTime to startTime to account for the gap after the last event
        startTime.append(eventTime)
        # Prepend 0 to endTime to represent the start of the timeline
        endTime = [0] + endTime
        # Get the total number of events (including eventTime)
        N = len(endTime)
        # List to store time gaps between consecutive events
        time_gaps = []
        # Initialize maximum free time
        max_free_time = 0
        
        # Calculate time gaps between the end of one event and the start of the next
        for i in range(N):
            time_gaps.append((startTime[i] - endTime[i], i))
        
        # Find the three largest time gaps using a heap
        # NOTE: THE TOP 3 time gaps make sure we have next biggest gap even if both gaps are included in current window. 
        top_3_time_gaps = heapq.nlargest(3, time_gaps, key=lambda x: x[0])
        
        # Iterate through events to calculate maximum free time
        for i in range(1, N):
            # Calculate the duration of the meeting between consecutive events
            meeting_duration = endTime[i] - startTime[i - 1]
            # Sum the gaps before and after the current event
            free_time = time_gaps[i][0] + time_gaps[i-1][0]
            # Check if any of the top 3 gaps can replace the meeting duration
            for gap, index in top_3_time_gaps:
                # Ensure the gap is not from the current or previous event
                if index not in [i, i-1] and gap >= meeting_duration:
                    # Add the meeting duration to free time if a suitable gap is found
                    free_time += meeting_duration
                    break
            # Update the maximum free time if the current free time is larger
            max_free_time = max(max_free_time, free_time)
        
        # Return the maximum free time found
        return max_free_time