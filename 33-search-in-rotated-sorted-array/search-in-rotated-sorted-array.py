class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left )//2
            if nums[mid] == target:
                return mid
            # print(mid, nums[mid], nums[l], l, r)
            if nums[mid] < nums[right]:
                # regular right split
                # irregulart ledt split
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # regular left split
                # irregulart right split
                if target > nums[mid]:
                    # target greter thanmiddle value and left part is soerted.
                    # then we can only find the required item in right partition. 
                    left = mid + 1
                elif target < nums[left]:
                    # target is less than middle value and less than left most value.
                    left = mid + 1
                else:
                    right = mid - 1 
        return -1