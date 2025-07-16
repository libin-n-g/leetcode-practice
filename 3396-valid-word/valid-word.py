class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        present_vowels = present_consonent = False
        for i in range(n):
            letter = word[i].lower()
            if letter in 'aeiou':
                present_vowels = True
            elif letter.isalpha() :
                present_consonent = True
            elif letter.isnumeric():
                continue
            else:
                return False
        return present_vowels & present_consonent