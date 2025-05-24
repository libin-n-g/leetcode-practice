class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        def isDivisor(s):
            l = len(s)
            if n1 % l != 0 and n2 % l != 0:
                return False
            if s * (n1//l) == str1 and s * (n2//l) == str2:
                return True
            return False
        for i in range(min(n1, n2), 0, -1):
            ret = str1[:i]
            if isDivisor(ret):
                return ret
        return ""
        