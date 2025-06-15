class Solution:
    def maxDiff(self, num: int) -> int:
        digits = deque()
        while num:
            digits.appendleft(num % 10)
            num = num // 10
        N = len(digits)
        # get first X
        i = 0
        first_x = first_y = 9
        while i < N and digits[i] == 9: i+= 1
        if i < N:
            first_x = digits[i]
        # first Y is always 9
        first_y = 9

        # get second X
        i = 0
        second_x = second_y = 1
        while i < N and digits[i] <= 1: i+=1
        if i < N: second_x = digits[i]
        # get second Y
        if i != 0 and i < N : second_y = 0
        print(first_x, first_y, second_x, second_y)
        new_num = 0
        for x in digits:
            if x == first_x == second_x:
                x = (first_y - second_y)
            elif x == first_x:
                x = first_y - x
            elif x == second_x:
                x = x - second_y
            else:
                x = 0
            new_num = new_num*10 + x
        return new_num
        