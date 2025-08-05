class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        current_types = defaultdict(int)
        i = 0
        max_window = 0
        for j, f in enumerate(fruits):
            current_types[f] += 1
            while len(current_types) > 2:
                current_types[fruits[i]] -= 1
                if current_types[fruits[i]] == 0:
                    del current_types[fruits[i]]
                i += 1
            max_window = max(max_window, j - i + 1)
            # print(current_types)
        return max_window