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
                while stack[-1][0] >= val:
                    stack.pop()
                height, index, previous_count = stack[-1]
                curr_count = val * (j - index) + previous_count
                count += curr_count
                stack.append((val, j, curr_count))
        return count
                