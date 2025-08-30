class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rule_checker = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_num = (i // 3) * 3 + j // 3
                keys = [f"col{j}", f"row{i}", f"box{box_num}"]
                for k in keys:
                    if board[i][j] in rule_checker[k]:
                        return False
                    rule_checker[k].add(board[i][j])
        return True