class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Dictionary to store the most recent index of each card
        indexes = {}
        # Dictionary to store the minimum distance for each card value
        min_distance_map = {}
        # Initialize return value as infinity to find minimum
        ret = float('inf')
        
        # Iterate through cards with index
        for i, c in enumerate(cards):
            # If card value seen before, calculate distance to previous occurrence
            if c in indexes:
                # Distance is current index minus previous index plus 1
                min_distance = i - indexes[c] + 1
                # If card not in min_distance_map, add it and update ret
                if c not in min_distance_map:
                    min_distance_map[c] = min_distance
                    ret = min(min_distance, ret)
                # If new distance is smaller, update min_distance_map and ret
                elif min_distance_map[c] > min_distance:
                    min_distance_map[c] = min_distance
                    ret = min(min_distance, ret)
            # Update the most recent index for this card
            indexes[c] = i
        
        # Return -1 if no matching cards found, otherwise return minimum distance
        return -1 if ret == float('inf') else ret
        