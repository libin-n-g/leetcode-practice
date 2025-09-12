class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel_count = 0
        vowel_letters = set(list("aeiou"))
        for c in s:
            if c in vowel_letters:
                vowel_count += 1
        if vowel_count == 0:
            return False
        return True

