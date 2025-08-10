class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quickselect(low, high, k):
            if high <= low:
                return nums[low]
            pivot = nums[high]
            starting_index = low
            for i in range(low, high):
                if nums[i] < pivot:
                    nums[i], nums[starting_index] = nums[starting_index], nums[i]
                    starting_index += 1
            nums[high], nums[starting_index] = nums[starting_index], nums[high]
            starting_index += 1
            if starting_index - low == k:
                return nums[starting_index-1]
            elif starting_index - low - 1 >= k:
                return quickselect(low, starting_index - 2, k)
            else:
                return quickselect(starting_index, high,  k - starting_index + low)
        n = len(nums)
        def virtual_index(i):
            # Calculates the virtual index using the formula (1 + 2*i) % (n | 1)
            # - 'i' is the input index to be mapped
            # - 'n' is the length of the array (assumed to be defined in the outer scope)
            # - 'n | 1' performs a bitwise OR with 1, ensuring the modulus is odd (n or n+1 for odd n)
            # - The formula (1 + 2*i) maps indices to alternate between odd and even positions
            # - The modulo operation ensures the result wraps around to stay within array bounds
            # - This creates a pattern like [1, 3, 5, ..., 0, 2, 4, ...] for placing elements
            return (1 + 2 * i) % (n | 1)
        median = quickselect(0, n-1, ((n+1) // 2) +1)
        left, right = 0, n-1
        i = 0
        while i < right:
            vi = virtual_index(i)
            if nums[vi] > median:
                left_vi = virtual_index(left)
                nums[left_vi], nums[vi] = nums[vi], nums[left_vi]
                left += 1
                i += 1
            elif nums[vi] < median:
                right_vi = virtual_index(right)
                nums[right_vi], nums[vi] = nums[vi], nums[right_vi]
                right -= 1
            else:
                i += 1


