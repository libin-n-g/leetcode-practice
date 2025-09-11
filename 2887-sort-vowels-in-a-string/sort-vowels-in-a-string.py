class Solution:
    def sortVowels(self, s: str) -> str:
        word = [ ]
        vowels = []
        for c in s:
            if c not in "aeiouAEIOU":
                word.append(c)
            else:
                word.append("_")
                vowels.append(c)
        j = 0
        vowels.sort()
        for i, c in enumerate(word):
            if c == "_":
                word[i] = vowels[j]
                j += 1
        return "".join(word)