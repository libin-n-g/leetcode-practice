class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        list_digits = list(str(n))
        counter = Counter(list_digits)
        list_digits.sort(reverse=True)
        largest_num_str = int("".join(list_digits))
        n = 1
        while n <= largest_num_str:
            if counter == Counter(str(n)):
                return True
            n = n << 1
        return False