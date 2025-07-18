class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)//3
        first_part = []
        second_part = []
        #sum_first - sum_second should be mininum. Means sum_first should be small and sum_second should be big
        # We need to replace largest element with a smaller element in first part to reduce the first sum.
        # Similarly we need to replace smaller element with larget element in second part to increase second sum.
        for i in range(N):
            # As by default we have min heap in python. We need to pop and compare with largest element in heap.
            first_part.append(-nums[i])
            second_part.append(nums[-i-1])
        heapify(first_part)
        heapify(second_part)
        current_first_part_sum = -sum(first_part)
        best = current_first_part_sum
        first_part_sums = [current_first_part_sum]
        for i in range(N,N*2):
            if nums[i] < -first_part[0]:
                current_first_part_sum += heappop(first_part) + nums[i]
                heappush(first_part, -nums[i])
            first_part_sums.append(current_first_part_sum)
        current_second_part_sum = sum(second_part)
        second_part_sums = [current_second_part_sum]
        best -= current_second_part_sum
        for i in range(N*2 - 1, N - 1, -1):
            if nums[i] > -second_part[0]:
                current_second_part_sum += -heappop(second_part) + nums[i]
                heappush(second_part, nums[i])
            second_part_sums.append(current_second_part_sum)
        second_part_sums.reverse()
        for x, y in zip(first_part_sums, second_part_sums):
            best = min(best, x-y)
        return best