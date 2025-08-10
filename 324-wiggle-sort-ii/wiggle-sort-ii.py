class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Step 1: Sort the array in-place
        nums.sort()  # O(n log n) time, O(1) space
        
        # Step 2: Create temporary array for rearrangement
        temp = [0] * n
        mid = (n - 1) // 2  # Index of the middle element
        right = n - 1       # Index of the largest element
        
        # Step 3: Fill temp array: even indices from mid downwards, odd indices from right downwards
        for i in range(n):
            if i % 2 == 0:
                temp[i] = nums[mid]
                mid -= 1
            else:
                temp[i] = nums[right]
                right -= 1
        
        # Step 4: Copy temp back to nums
        for i in range(n):
            nums[i] = temp[i]