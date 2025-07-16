class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        if not word.isalnum():
            return False
        present_vowels = present_consonent = False
        for i in range(n):
            if word[i].lower() in 'aeiou':
                present_vowels = True
            elif word[i].lower().isalpha() :
                present_consonent = True
        return present_vowels and present_consonent