class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        edges = [] 
        # do BFS
        end_node = n*n
        queue = deque([(1, 0)])
        visited_nodes = {1}
        while queue:
            curr_node, distance = queue.popleft()
            if curr_node == end_node:
                return distance
            for i in range(curr_node + 1, min(curr_node + 6, end_node) + 1):
                row_index = ((i-1)//n)
                column_index = (i-1) % n
                if row_index % 2 == 1:
                    column_index = n - column_index - 1
                row_index = n - row_index - 1
                go_to_node = board[row_index][column_index]
                if go_to_node != -1:
                    if go_to_node not in visited_nodes:
                        queue.append((go_to_node, distance + 1))
                        visited_nodes.add(go_to_node)
                elif i not in visited_nodes:
                    queue.append((i, distance + 1))
                    visited_nodes.add(i)
        return -1
