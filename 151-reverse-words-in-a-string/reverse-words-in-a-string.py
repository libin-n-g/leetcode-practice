class Solution:
    def reverseWords(self, s: str) -> str:
        ret = []
        for w in s.split(' '):
            if w != "":
                ret.append(w.strip())
        return " ".join(ret[::-1]) 