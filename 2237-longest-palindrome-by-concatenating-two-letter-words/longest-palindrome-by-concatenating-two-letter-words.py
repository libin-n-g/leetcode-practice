class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        center_selected = False
        for w in count:
            if w[0] == w[1]:
                if not center_selected and count[w] % 2 == 1:
                    length += 2
                    center_selected = True
                length += (count[w] // 2 )*4
            elif w[::-1] in count:
                length += min(count[w], count[w[::-1]])*2
        return length
            