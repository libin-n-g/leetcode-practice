class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        edges = []
        n = len(board)
        queue = deque(board)
        order = 1
        while queue:
            row = queue.pop()
            edges.extend(row[::order])
            order = 0-order    
        # do BFS
        end_node = n*n
        queue = deque([(1, -1, 0)])
        visited_nodes = [1]
        while queue:
            curr_node, parent, distance = queue.popleft()
            if curr_node == end_node:
                return distance
            found = False
            last_accessable_node = min(curr_node + 6, end_node)
            for i in range(curr_node + 1, last_accessable_node + 1):
                if edges[i-1] != -1:
                    if edges[i-1] not in visited_nodes:
                        queue.append((edges[i-1], curr_node, distance + 1))
                        visited_nodes.append(edges[i-1])
                elif i not in visited_nodes:
                    queue.append((i, curr_node, distance + 1))
                    visited_nodes.append(i)
        return -1
