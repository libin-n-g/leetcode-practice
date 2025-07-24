class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        first_condition, second_condition = "ab", "ba"
        if x < y:
            x, y = y, x
            first_condition, second_condition = second_condition, first_condition
        first_condition_stack = []
        score = 0
        for c in s:
            if first_condition_stack and \
                first_condition[0] == first_condition_stack[-1] and first_condition[1] == c:
                score += x
                first_condition_stack.pop()
            else:
                first_condition_stack.append(c)
        second_condition_stack = []
        for c in first_condition_stack:
            if second_condition_stack and second_condition[0] == second_condition_stack[-1] and second_condition[1] == c:
                score += y
                second_condition_stack.pop()
            else:
                second_condition_stack.append(c)
        return score 
            