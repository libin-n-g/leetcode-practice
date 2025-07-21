class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if stack and c != stack[-1]:
                count = 0
            stack.append(c)
            count += 1
            if count >= 3:
                stack.pop()
                count -= 1
        return "".join(stack)
