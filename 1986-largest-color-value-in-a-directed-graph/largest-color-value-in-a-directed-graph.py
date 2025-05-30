from collections import deque
from collections import defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Number of nodes in the graph
        num_nodes_to_visit = len(colors)
        # dp[i] stores a dictionary mapping colors to their max frequency in paths ending at node i
        dp = [defaultdict(int) for _ in range(num_nodes_to_visit)]
        # Adjacency list to store graph edges (node -> list of neighbors)
        edges_map = defaultdict(list)
        # Store in-degree (number of incoming edges) for each node
        indegree = defaultdict(int)
        # Initialize result to track max color frequency
        res = 0 
        
        # Build adjacency list and in-degree map
        for start, end in edges:
            edges_map[start].append(end)  # Add directed edge from start to end
            indegree[end] += 1           # Increment in-degree of end node
        
        # Initialize queue for Kahn's Algorithm with nodes having in-degree 0
        queue = deque()
        for node in range(num_nodes_to_visit):
            if indegree[node] == 0:
                queue.append(node)        # Add nodes with no incoming edges to queue
        
        # Process nodes using Kahn's Algorithm (topological sort)
        while queue:
            current_index = queue.pop()   # Get next node with in-degree 0
            current_color = colors[current_index]  # Get color of current node
            # Increment frequency of current node's color in its dp entry
            dp[current_index][current_color] += 1
            # Update max color frequency seen so far
            res = max(res, dp[current_index][current_color])
            
            # Process all neighbors of current node
            for node in edges_map[current_index]:
                indegree[node] -= 1      # Decrease in-degree of neighbor
                # Propagate color frequencies from current node to neighbor
                for c in dp[current_index]:
                    if dp[current_index][c] > dp[node][c]:
                        # Update neighbor's color frequency if current path gives higher value
                        dp[node][c] = dp[current_index][c]
                        # Update result with max frequency seen
                        res = max(res, dp[node][c])
                # If neighbor's in-degree becomes 0, add it to queue
                if indegree[node] == 0:
                    queue.append(node)
            num_nodes_to_visit -= 1 # Just decrementing number pf nodes to make sure all nodes are visted. (cycle detection)
        
        # If num_nodes == 0 (number of nodes left to visit), graph has a cycle, return -1
        return -1 if num_nodes_to_visit != 0 else res