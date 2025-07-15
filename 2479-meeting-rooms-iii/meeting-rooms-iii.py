import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        room_count = defaultdict(int)
        occupied_room_heap = [(-1, 0)]
        free_rooms = list(range(1, n)) 
        heapq.heapify(free_rooms)
        # print(meetings)
        wait_time = 0
        for s, e in meetings:
            while occupied_room_heap and occupied_room_heap[0][0] <= s:
                _, room_num = heapq.heappop(occupied_room_heap)
                heapq.heappush(free_rooms, room_num)
            if free_rooms:
                room_num = heapq.heappop(free_rooms)
                room_count[room_num] += 1
                heapq.heappush(occupied_room_heap, (e, room_num))
            else:
                end_time, room_num = heapq.heappop(occupied_room_heap)
                wait_time = (end_time - s)
                room_count[room_num] += 1
                heapq.heappush(occupied_room_heap, (e + wait_time, room_num))
            # print(occupied_room_heap)
        max_room = 0
        # print(room_count)
        for i in room_count:
            if room_count[max_room] < room_count[i]:
                max_room = i
        return max_room