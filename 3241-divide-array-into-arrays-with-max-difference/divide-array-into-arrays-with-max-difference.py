class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Step 1: Sort the array to minimize differences within each triplet
        # Sorting ensures that consecutive elements are as close as possible,
        # which is optimal for forming triplets with max difference <= k
        nums.sort()
        
        # Initialize result to store the triplets
        result = []
        
        # Step 2: Iterate over the sorted array in steps of 3
        # Since n is a multiple of 3, we process elements in groups of 3
        for i in range(0, len(nums), 3):
            # Step 3: Check if the triplet satisfies the condition
            # For triplet [nums[i], nums[i+1], nums[i+2]], the max difference
            # is nums[i+2] - nums[i] (since array is sorted)
            # If this difference exceeds k, no valid solution is possible
            if nums[i+2] - nums[i] > k:
                return []
            
            # Step 4: Add the valid triplet to the result
            result.append(nums[i:i+3])
        
        # Step 5: Return the list of triplets
        return result

        # Proof of Completeness:
        # The algorithm finds a valid solution if one exists. Here's why:
        # - A valid solution partitions n elements into n/3 triplets, each with
        #   max difference <= k.
        # - Sorting minimizes the difference within each triplet, as consecutive
        #   elements in the sorted array are closest together.
        # - If a valid solution exists, it must use all n elements. Suppose the
        #   algorithm fails (returns []) because some triplet [nums[i], nums[i+1],
        #   nums[i+2]] has nums[i+2] - nums[i] > k. In any valid partition, these
        #   elements must be grouped somehow. However, any grouping that spreads
        #   elements across a wider range in the sorted array would result in an
        #   even larger difference. Thus, if sorted consecutive triplets fail, no
        #   other grouping can satisfy the condition.
        # - Therefore, if a solution exists, grouping sorted consecutive triplets
        #   will find it, ensuring completeness.