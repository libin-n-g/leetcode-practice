from string import ascii_lowercase
class Solution:
    # def robotWithString(self, s: str) -> str:
        # i = 0
        # t = []
        # paper = ""
        # for c in ascii_lowercase:
        #     if c not in c:
        #         continue
        #     else:
        #         while t and t[-1] <= c:
        #             paper += t.pop()
        #         while c in s:
        #             while s[-1] != c:

    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        p = ""
        t = []
        smallest_freq_char = "a"
        for c in s:
            t.append(c)
            counter[c]-=1
            while len(t) > 0:
                while ord(smallest_freq_char) < ord('z') + 1:
                    if counter[smallest_freq_char] > 0:
                        break
                    smallest_freq_char = chr(ord(smallest_freq_char) + 1)
                if t[-1] > smallest_freq_char:
                    break
                else:
                    p += t.pop()
        return p