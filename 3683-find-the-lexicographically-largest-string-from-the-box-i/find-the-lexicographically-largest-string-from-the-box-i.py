class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        starting = 0
        if numFriends == 1:
            return word
        # r = len(word) - 1 - numFriends
        for l in range(len(word)):
            if word[l:l+len(word) - numFriends + 1] > word[starting:starting+len(word) - numFriends + 1]:
                starting=l
        return word[starting:starting+len(word) - numFriends + 1] 