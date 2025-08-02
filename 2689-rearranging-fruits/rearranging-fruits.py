class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = Counter(basket1)
        min_value = min(min(basket1), min(basket2))
        for item in basket2:
            counter[item] -= 1
        trasfer_array = []
        for item, freq in counter.items():
            if freq % 2 == 1:
                return -1
            trasfer_array.extend([item] * (abs(freq) // 2))
        trasfer_array.sort()
        cost = 0
        for i in trasfer_array[:len(trasfer_array)//2]:
            cost += min(2*min_value, i)
        return cost