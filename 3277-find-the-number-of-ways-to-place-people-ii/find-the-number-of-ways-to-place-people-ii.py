class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort the points by their x-coordinate, and then by their y-coordinate in descending order
        points.sort(key=lambda point: (point[0], -point[1]))
        ans = 0  # Initialize the number of valid pairs to zero
      
        # Iterate over each point
        for i, (_, y1) in enumerate(points):
            max_y = -inf  # Initialize the maximum y-value for the points considered so far

            # Compare with subsequent points to check for pairs
            for _, y2 in points[i + 1:]:
                # If the y-value of the current point is greater than max_y
                # and not greater than y1, this is a valid pair
                if max_y < y2 <= y1:
                    max_y = y2  # Update max_y to the current y-value
                    ans += 1  # Increment the count of valid pairs

        return ans  # Return the total number of valid pairs found
