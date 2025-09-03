class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort the points by their x-coordinate, and then by their y-coordinate in descending order
        points.sort(key=lambda point: (point[0], -point[1]))
        count = 0  
        # Lets select point A where Alice is at. 
        # Note that it starts from top left corner (because of sorting)
        for i, (_, y1) in enumerate(points):
            # Now lets select a point which is right and down of point B (x2, y2) where bob is at.
            # x2 >= x1 and y2 <= y1 (always true because of sorting)
            y_max = -inf
            for _, y2 in points[i+1:]:
                # if x3, y3 is another point other than A and B, 
                # then we need to make sure the points does not satisfy the following condition
                # x2 >= x3 >= x1 and y2 <= y3 <= y1.
                # For any point we have seen before (x3, y3) current B should have x2 >= x3. 
                # if x2 == x3 then y2 <= y3. First condition is anyway satisfied weneed to count points not satifiing second condition. 
                if y_max < y2 <= y1:
                    count += 1
                    y_max = y2
        return count  # Return the total number of valid pairs found