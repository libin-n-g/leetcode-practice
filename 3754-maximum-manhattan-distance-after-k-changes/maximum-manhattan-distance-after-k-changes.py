class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # Initialize a defaultdict to count occurrences of each direction ('N', 'S', 'E', 'W')
        distance_mapping = defaultdict(int)
        # Track the maximum Manhattan distance achieved
        max_distance = 0
        pairs = [("N", "S"), ("W", "E")]
        # Iterate through each character in the input string
        for c in s:
            # Increment the count for the current direction
            distance_mapping[c] += 1
            # Copy the number of allowed changes (k) for this iteration
            ck = k
            distance = 0
            for d1, d2 in pairs:
                # Determine the maximum and minimum counts for north-south movements
                if distance_mapping[d1] > distance_mapping[d2]:
                    x_max = distance_mapping[d1]
                    x_min = distance_mapping[d2]
                else:
                    x_max = distance_mapping[d2]
                    x_min = distance_mapping[d1]
                    
                # Calculate how many changes can be made to minimize the smaller count
                # This effectively maximizes the difference between N and S
                delta = min(ck, x_min)
                x_max += delta  # Increase the larger count by the number of changes
                x_min -= delta  # Decrease the smaller count by the number of changes
                ck -= delta     # Update remaining allowed changes
                distance += (x_max - x_min)
            max_distance = max(max_distance, distance)
        
        # Return the maximum Manhattan distance achieved
        return max_distance