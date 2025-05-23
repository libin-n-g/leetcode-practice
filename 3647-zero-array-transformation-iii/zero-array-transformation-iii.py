class Solution:
    def maxRemoval(self, nums: list[int], queries: list[list[int]]) -> int:
        query_start_ends_map = defaultdict(list)
        for s, e in queries:
            query_start_ends_map[s].append(e)
        used_queries_array, available_heap, current_usable_queries = [0]*(len(nums)+1), [], 0
        for index, num in enumerate(nums):
            for end in query_start_ends_map[index]:
                heappush(available_heap, -end)
            current_usable_queries += used_queries_array[index]
            while current_usable_queries < num:
                # get valid item or item we got is already too less. Which means we cannot find valid anymore. 
                if not available_heap or -available_heap[0] < index:
                    return -1
                end = -heappop(available_heap)
                current_usable_queries += 1
                used_queries_array[end + 1] -= 1
        return len(available_heap)

    def maxRemoval_two_heaps(self, nums: List[int], queries: List[List[int]]) -> int:
        avilable_query_heap = []
        used_queary_min_heap = []
        queries.sort()
        num_used_quaries = 0
        q_idx = 0
        q_length = balance_quaries = len(queries)
        for i in range(len(nums)):
            while q_idx < q_length and queries[q_idx][0] <= i:
                heapq.heappush(avilable_query_heap, -queries[q_idx][1])
                q_idx += 1
                # print(f"INSERT [{i}, {e}] to available pool")
            nums[i] -= len(used_queary_min_heap)
            while nums[i] > 0 and avilable_query_heap:
                e = -heapq.heappop(avilable_query_heap)
                if e >= i:
                    heapq.heappush(used_queary_min_heap, e)
                    # print(f"Use new [{i}, {e}] to used pool")
                    nums[i] -= 1
                    balance_quaries -= 1
            if nums[i] > 0:
                return -1
            while used_queary_min_heap and used_queary_min_heap[0] <= i:
                heapq.heappop(used_queary_min_heap)
        return balance_quaries

