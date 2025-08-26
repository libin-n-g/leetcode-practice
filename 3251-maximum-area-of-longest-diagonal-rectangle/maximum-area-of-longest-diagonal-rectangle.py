class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diags = [l*l + w*w for l, w in dimensions]
        max_diag = max(diags)
        return max([dimensions[i][0]*dimensions[i][1] for i in range(len(diags)) if max_diag == diags[i]])