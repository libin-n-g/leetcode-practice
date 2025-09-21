class Spreadsheet:
    columns_label = set(list("QWERTYUIOPASDFGHJKLZXCVBNM"))
    digits = set(list("1234567890"))
    def __init__(self, rows: int):
        self.columns = defaultdict(lambda : [0]*rows)
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        col, row = cell[0], int(cell[1:]) - 1
        self.columns[col][row] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        current_value = ""
        return_value = 0
        row = None
        for c in formula[1:]:
            if c in self.columns_label:
                row = self.columns[c]
            elif c in self.digits:
                current_value += c
            else:
                if row:
                    return_value += row[int(current_value) - 1]
                else:
                    return_value += int(current_value)
                row = None
                current_value = ""
        if row:
            return_value += row[int(current_value) - 1]
        else:
            return_value += int(current_value)
        return return_value


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)