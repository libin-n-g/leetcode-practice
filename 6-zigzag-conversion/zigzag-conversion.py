class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""]
        curr_row = 0
        sign = 1
        for c in s:
            if len(rows) == curr_row:
                rows.append("")
            rows[curr_row] += c
            if curr_row == numRows - 1 and sign == 1:
                sign = -1
            elif curr_row == 0 and sign == -1 :
                sign = +1
            curr_row += sign
        return "".join(rows)

