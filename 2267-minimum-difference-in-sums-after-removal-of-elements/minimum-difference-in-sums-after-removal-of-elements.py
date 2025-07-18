from heapq import heapify, heappop, heappush

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # N is the number of elements in each part after removing n elements
        # Total length is 3n, so each part (first, second, removed) has n elements
        N = len(nums) // 3
        
        # Initialize min-heaps for first and second parts
        # first_part will store negative values to simulate a max-heap
        first_part = []
        second_part = []
        
        # Goal: Minimize sum_first - sum_second
        # To achieve this, we want sum_first to be as small as possible
        # and sum_second to be as large as possible
        
        # Initialize first_part with first N elements (negated for max-heap)
        # Initialize second_part with last N elements
        for i in range(N):
            # Negate numbers for first_part to use min-heap as max-heap
            first_part.append(-nums[i])
            # Use last N elements for second_part
            second_part.append(nums[-i-1])
        
        # Convert lists to heaps
        heapify(first_part)
        heapify(second_part)
        
        # Calculate initial sum of first_part (negate back to get actual sum)
        current_first_part_sum = -sum(first_part)
        # Initialize best difference as the initial first_part sum
        # (will subtract second_part sum later)
        best = current_first_part_sum
        # Store sums of first_part for each possible configuration. 
        # ie, What is min value possible with N + i values (counted from the start) is stored at ith index.
        first_part_sums = [current_first_part_sum]
        
        # Process middle N elements (indices N to 2N-1)
        # For each element, decide whether to include it in first_part
        # to minimize the sum
        for i in range(N, N*2):
            # If current element is smaller than the largest in first_part
            # (remember first_part[0] is negative, so -first_part[0] is largest)
            if nums[i] < -first_part[0]:
                # Remove largest element (add it back since negated)
                current_first_part_sum += heappop(first_part) + nums[i]
                # Add new element (negated)
                heappush(first_part, -nums[i])
            # Store the sum after each step
            first_part_sums.append(current_first_part_sum)
        
        # Calculate initial sum of second_part
        current_second_part_sum = sum(second_part)
        # Store sums of second_part for each possible configuration
        # ie, What is max value possible with N + i values (counted from the end) is stored at ith index.
        second_part_sums = [current_second_part_sum]
        # Update best difference with initial sums
        best -= current_second_part_sum
        
        # Process middle N elements in reverse (indices 2N-1 to N)
        # For each element, decide whether to include it in second_part
        # to maximize the sum
        for i in range(N*2 - 1, N - 1, -1):
            # If current element is larger than the smallest in second_part
            if nums[i] > second_part[0]:
                # Remove smallest element and add new element
                current_second_part_sum += -heappop(second_part) + nums[i]
                heappush(second_part, nums[i])
            # Store the sum after each step
            second_part_sums.append(current_second_part_sum)
        
        # Reverse second_part_sums to align with first_part_sums
        # Because we need to remove n elemets in total. 
        # ie. if we remove 1 elemnt from forst part, we need to remove n-1 elements from second part.
        second_part_sums.reverse()
        
        # Find minimum difference by comparing all valid pairs of sums
        for x, y in zip(first_part_sums, second_part_sums):
            best = min(best, x - y)
        
        return best