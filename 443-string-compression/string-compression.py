class Solution:
    def compress(self, chars: List[str]) -> int:
        final_length = 0
        i = 0
        while i < len(chars):
            c = chars[i]
            group_count = 0
            while i + group_count < len(chars) and c == chars[i + group_count]:
                group_count += 1
            chars[final_length] = c
            final_length+=1
            if group_count > 1:
                for digit in str(group_count):
                    chars[final_length] = digit
                    final_length+=1
            i += group_count
        return final_length
            
        # count = 1
        # char = chars[0]
        # i = 0
        # while i < len(chars):
        #     char = chars[i]
        #     count = 1
        #     i += 1
        #     count_index = i
        #     while i < len(chars) and char == chars[i]:
        #         count+=1
        #         chars.pop(i)
        #     if count == 1:
        #         continue
        #     for j, s in enumerate(str(count)):
        #         chars.insert(count_index + j,  s)
        #         i += 1
        # return len(chars)
