class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        distance_mapping = defaultdict(int)
        opposites = {
            "N": "S",
            "S": "N",
            "W": "E",
            "E": "W"
        }
        max_distance = 0
        for c in s:
            distance_mapping[c] += 1
            if distance_mapping["N"] > distance_mapping["S"]:
                x_max = distance_mapping["N"]
                x_min = distance_mapping["S"]
            else:
                x_max = distance_mapping["S"]
                x_min = distance_mapping["N"]
            ck = k
            delta = min(ck, x_min)
            x_max += delta
            x_min -= delta
            ck -= delta

            if distance_mapping["W"] > distance_mapping["E"]:
                y_max = distance_mapping["W"]
                y_min = distance_mapping["E"]
            else:
                y_max = distance_mapping["E"]
                y_min = distance_mapping["W"]
            delta = min(ck, y_min)
            y_max += delta
            y_min -= delta
            ck -= delta
            max_distance = max(max_distance, (x_max - x_min) + (y_max - y_min))
        return max_distance