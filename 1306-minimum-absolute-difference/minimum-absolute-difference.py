class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sort the input array to ensure adjacent elements are compared for minimum difference
        arr_sorted = sorted(arr)
        # Initialize result list to store pairs with minimum absolute difference
        result = []
        # Initialize minimum difference as infinity to find the smallest difference
        min_diff = float('inf')
        # Iterate through sorted array, comparing adjacent elements
        for i, a in enumerate(arr_sorted[:-1]):
            # Get the next element in the sorted array
            b = arr_sorted[i+1]
            # Calculate absolute difference between current and next element
            diff = b - a
            # Check if current difference is less than or equal to the minimum found so far
            if diff <= min_diff:
                # If difference equals current minimum, add pair to result
                if diff == min_diff:
                    result.append([a, b])
                # If difference is smaller, reset result with new pair and update min_diff
                else:
                    result = [[a, b]]
                min_diff = diff
        # Return list of pairs with minimum absolute difference
        return result