class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        counterp = Counter(p)
        counter_sliding = Counter(s[:len_p])
        ret = []
        if counterp == counter_sliding:
            ret.append(0)
        for i in range(len_p, len(s)):
            counter_sliding[s[i-len_p]] -= 1
            counter_sliding[s[i]] += 1
            if counterp == counter_sliding:
                ret.append(i-len_p+1)
        return ret