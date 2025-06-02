class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        char = chars[0]
        i = 0
        while i < len(chars):
            char = chars[i]
            count = 1
            i += 1
            count_index = i
            while i < len(chars) and char == chars[i]:
                count+=1
                chars.pop(i)
            if count == 1:
                continue
            for j, s in enumerate(str(count)):
                chars.insert(count_index + j,  s)
                i += 1
        return len(chars)
