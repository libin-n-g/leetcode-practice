class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) -1
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        while l < r:
            case1 = s[r].lower() in vowels
            case2 = s[l].lower() in vowels
            if case1 and case2:
                # swap, progress both index
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            elif case1 and not case2:
                # only progress l 
                l += 1
            elif not case1 and case2:
                # oly progress r
                r -= 1
            else:
                #progress both
                l+=1
                r-=1
        return "".join(s)