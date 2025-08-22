class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0
        histogram = [0]*len(mat[0])
        for row in mat:
            for j, val in enumerate(row):
                if val == 0:
                    histogram[j] = 0
                else:
                    histogram[j] += 1
            stack = [(-1, -1, 0)] # height, index, previous_count
            for j, val in enumerate(histogram):
                # find the index where height decreses.
                while stack[-1][0] >= val:
                    stack.pop()
                height, index, previous_count = stack[-1]
                # (j - index) is gap. 
                # Note that placeholder -1 will helps in getting correct gap when there is no element less that current
                """
                aSSUME BELOW STRUCTURE IN MATRIX
                      |  |  |  |
                |  |  |  |  |  |
                |  | a|  |  | b|
                Gap is 3 here. Total number of submtrix ending at b is (3*b) + a. Let a and b be 1 heights(histogram)
                """
                curr_count = val * (j - index) + previous_count
                count += curr_count
                stack.append((val, j, curr_count)) # Note that the j (index) only increses.
                # hence stack will contain highest index at left most and decreses as it gets poped.
        return count
                