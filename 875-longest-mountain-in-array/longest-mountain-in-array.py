class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length = 0
        i = 1
        while i < len(arr)-1: # because we will not get peak in the end and begin
            # check if peak point
            if arr[i-1] < arr[i] > arr[i+1]:
                l = i - 1
                r = i + 1
                # find left vally end
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1
                # find right vally end
                while r < len(arr) - 1 and arr[r] > arr[r+1]:
                    r+=1
                max_length = max(max_length, r - l + 1)
                i = r
                continue
            i += 1
        return max_length
    def longestMountain_o2n(self, arr: List[int]) -> int:
        n = len(arr)
        l , r = 0, n - 1
        while l < r and arr[r] >= arr[r-1]:
            r -= 1
        while l < r and arr[l] >= arr[l+1]: 
            l += 1
        mountain_length = []
        mode = '-'
        while l < r:
            if arr[l] < arr[l+1] and mode != '+':
                mode = '+' 
                mountain_length.append(0)
            if arr[l] > arr[l+1] and mode != '-':
                mode = '-' 
                mountain_length.append(0)
            if arr[l] != arr[l+1]:
                if mode == '+':
                    mountain_length[-1]+=1
                else:
                    mountain_length[-1]-=1
            else: 
                if mode != '0':
                    mountain_length.append(0)
                    mode = '0'
                while l < r and arr[l] >= arr[l+1]: 
                    l += 1
                l -= 1
            l += 1
        max_mountaion_length = 0
        i = 1
        while i < len(mountain_length):
            if mountain_length[i] < 0 and mountain_length[i-1] > 0:
                max_mountaion_length = max(max_mountaion_length, mountain_length[i-1] - mountain_length[i] + 1)
            if mountain_length[i-1] == 3:
                print(mountain_length[i-1], mountain_length[i], i)
            else:
                i += 1
                continue
            i += 2
        return max_mountaion_length