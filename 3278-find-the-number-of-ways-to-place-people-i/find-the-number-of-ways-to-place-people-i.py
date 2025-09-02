class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[0], -point[1]))
        count = 0
        # Iterate through each point
        for i, (_, y1) in enumerate(points):
            max_y = -inf  # Initialize the maximum y as negative infinity
          
            # Compare with other points that come after the current one
            for _, y2 in points[i + 1:]:
                # If there is a point with a y-coordinate less than or equal to y1 but greater than max_y
                if max_y < y2 <= y1:
                    max_y = y2  # Update the max_y
                    count += 1  # Increment the number of pairs
      
        return count  # Return the total number of valid pairs found