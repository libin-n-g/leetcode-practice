class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        # Initialize a queue with the initial boxes that can be opened
        queue = deque(initialBoxes)
        # Track visited boxes that can't be opened yet due to missing keys
        unable_to_open_visited = set()
        # Initialize the total candies collected
        ret = 0
        
        # Continue BFS while there are boxes to process
        while queue:
            # Get the next box to process from the front of the queue
            curr_node = queue.popleft()
            
            # Check if the current box can be opened (status is 1)
            if status[curr_node] == 1:
                # Add candies from the current box to the total
                ret += candies[curr_node]
                
                # Process all boxes contained within the current box
                for i in containedBoxes[curr_node]:
                    # No cycles possible as tree structure is guaranteed. 
                    queue.append(i) 
                
                # Process all keys found in the current box
                for i in keys[curr_node]:
                    # Unlock the box corresponding to this key
                    status[i] = 1
                    # If the unlocked box was previously unopenable, add it to the queue
                    if i in unable_to_open_visited:
                        queue.append(i)
                        # remove item from the set as this is no longer unopenable
                        unable_to_open_visited.remove(i)
            else:
                # If the box can't be opened (locked), add it to not_opened set
                unable_to_open_visited.add(curr_node)
        
        # Return the total number of candies collected
        return ret