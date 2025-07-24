class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ab_condition = lambda x, y: x == 'a' and y == 'b'
        ba_condition = lambda x, y: ab_condition(y, x) 
        if x < y:
            x, y = y, x
            first_condition = ba_condition
            second_condition = ab_condition
        else:
            first_condition = ab_condition
            second_condition = ba_condition
        stack = []
        score = 0
        for c in s:
            if stack and first_condition(stack[-1], c):
                score += x
                stack.pop()
            else:
                stack.append(c)
        stack_2 = []
        for c in stack:
            if stack_2 and second_condition(stack_2[-1], c):
                score += y
                stack_2.pop()
            else:
                stack_2.append(c)
        return score 
            