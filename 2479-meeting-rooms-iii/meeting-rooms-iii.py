import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Sort meetings by start time to process them in chronological order
        meetings.sort(key = lambda x : x[0])
        # Dictionary to count the number of meetings per room
        room_count = defaultdict(int)
        # Min-heap of occupied rooms: (end_time, room_number)
        # Initialize with a dummy entry to handle initial free rooms
        occupied_room_heap = [(-1, 0)]
        # Min-heap of free room numbers (1 to n-1 initially, as room 0 is in occupied heap)
        free_rooms = list(range(1, n)) 
        heapq.heapify(free_rooms)
        # Variable to track wait time for delayed meetings
        wait_time = 0
        
        # Process each meeting
        for s, e in meetings:
            # Free up rooms whose meetings have ended by the current meeting's start time
            while occupied_room_heap and occupied_room_heap[0][0] <= s:
                _, room_num = heapq.heappop(occupied_room_heap)
                heapq.heappush(free_rooms, room_num)
            
            # If there are free rooms, assign the meeting to the lowest-numbered free room
            if free_rooms:
                room_num = heapq.heappop(free_rooms)
                room_count[room_num] += 1
                heapq.heappush(occupied_room_heap, (e, room_num))
            # If no free rooms, delay the meeting until the earliest-ending meeting finishes
            else:
                end_time, room_num = heapq.heappop(occupied_room_heap)
                wait_time = end_time - s  # Calculate delay
                room_count[room_num] += 1
                # Schedule the meeting to start after the earliest-ending meeting
                heapq.heappush(occupied_room_heap, (e + wait_time, room_num))
        
        # Find the room with the maximum number of meetings
        max_room = 0
        for i in room_count:
            if room_count[max_room] < room_count[i]:
                max_room = i
        
        # Return the room number with the most meetings
        return max_room