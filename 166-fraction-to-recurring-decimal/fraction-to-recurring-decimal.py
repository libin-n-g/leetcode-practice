class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = False
        if numerator < 0:
            numerator = - numerator
            negative = not negative
        if denominator < 0:
            negative = not negative
            denominator = - denominator
        result = str(numerator//denominator)
        numerator = numerator % denominator
        fractions = []
        numerator_list = [numerator]
        seen_numerator = set(numerator_list)
        while numerator:
            numerator = 10*numerator
            if numerator in seen_numerator:
                numerator = numerator // 10
                break
            seen_numerator.add(numerator)
            curr_fraction = (str((numerator)//denominator))
            numerator = numerator % denominator
            fractions.append(curr_fraction)
            numerator_list.append(numerator)
        if fractions:
            result += "."
        for num, frac in zip(numerator_list, fractions):
            if num == numerator != 0:
                result += "("
            result += frac
        if "(" in result:
            result += ")"
        if negative and result != "0":
            result = "-" + result
        return result