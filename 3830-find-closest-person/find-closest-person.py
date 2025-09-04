class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Determines which of two numbers (x or y) is closest to a target number z.
      
        Args:
            x: First number to compare
            y: Second number to compare  
            z: Target number to measure distance from
          
        Returns:
            0 if x and y are equidistant from z
            1 if x is closer to z than y
            2 if y is closer to z than x
        """
        # Calculate absolute distance from x to z
        distance_x_to_z = abs(x - z)
      
        # Calculate absolute distance from y to z
        distance_y_to_z = abs(y - z)
      
        # Compare distances and return appropriate value
        if distance_x_to_z == distance_y_to_z:
            return 0  # Both are equidistant
        elif distance_x_to_z < distance_y_to_z:
            return 1  # x is closer
        else:
            return 2  # y is closer
