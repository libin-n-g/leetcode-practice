class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexes = {}
        min_distance_map = {}
        ret = float('inf')
        for i, c in enumerate(cards):
            if c in indexes:
                min_distance = i - indexes[c] + 1
                if c not in min_distance_map:
                    min_distance_map[c] = min_distance
                    ret =  min(min_distance, ret)
                elif min_distance_map[c] > min_distance:
                    min_distance_map[c] = min_distance
                    ret = min(min_distance, ret)
            indexes[c] = i
        return -1 if ret == float('inf') else ret
        