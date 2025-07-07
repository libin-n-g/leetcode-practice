class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # BACKTRACKING
        # result = []
        # def backtrack(sub="", i=0):
        #     if len(s) == i:
        #         result.append(sub)
        #         return
        #     if s[i].isalpha():
        #         backtrack(sub + s[i].swapcase(), i+1)
        #     backtrack(sub + s[i], i+1)
        # backtrack("", 0)
        result = ['']
        for c in s:
            for i in range(len(result)):
                sub = result[i]
                if c.isalpha():
                    result[i] = sub + c.lower()
                    result.append(sub + c.upper())
                else:
                    result[i] = sub + c
        return result