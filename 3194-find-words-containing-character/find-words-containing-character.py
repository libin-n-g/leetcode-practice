class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for i, w in enumerate(words):   
            if x in w:
                ret.append(i)
        return ret