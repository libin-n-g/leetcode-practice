class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = Counter(basket1)
        min_value = min(min(basket1), min(basket2))
        for item in basket2:
            counter[item] -= 1
        trasfer_array = []
        trasfer_count_half = 0
        for item in counter:
            if counter[item] % 2 == 1:
                return -1
            counter[item] = abs(counter[item])
            while counter[item] != 0:
                trasfer_array.append(item)
                counter[item] -= 2
                trasfer_count_half += 0.5
        trasfer_array.sort()
        cost = 0
        for i in trasfer_array[:int(trasfer_count_half)]:
            if i > 2*min_value:
                cost += 2*min_value
            else:
                cost += i
        return cost