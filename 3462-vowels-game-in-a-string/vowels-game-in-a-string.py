class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c in "aeiou":
                return True
        return False
        # c = Counter(s)
        # vowel_count = c["a"] + c["e"] + c["i"] + c["o"] + c["u"]
        vowel_count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
        # Count function for string is faster as the function runs in Cpython. 
        if vowel_count == 0:
            return False
        return True

