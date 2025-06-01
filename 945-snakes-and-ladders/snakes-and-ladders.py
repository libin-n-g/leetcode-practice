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
        print(edges)
        # do BFS
        end_node = n*n
        queue = deque([(1, -1, 0)])
        visited_nodes = [1]
        while queue:
            curr_node, parent, distance = queue.popleft()
            if curr_node == end_node:
                return distance
            found = False
            print(f"On Node {curr_node}")
            last_accessable_node = min(curr_node + 6, end_node)
            for i in range(curr_node + 1, last_accessable_node + 1):
                if edges[i-1] != -1:
                    if edges[i-1] not in visited_nodes:
                        queue.append((edges[i-1], curr_node, distance + 1))
                        visited_nodes.append(edges[i-1])
                        print(f"Adding {edges[i-1]}")
                elif i not in visited_nodes:
                    queue.append((i, curr_node, distance + 1))
                    visited_nodes.append(i)
                    print(f"Adding {last_accessable_node}")
                # elif i == last_accessable_node:
                #     if last_accessable_node not in visited_nodes:
                #         queue.append((last_accessable_node, curr_node, distance + 1))
                #         visited_nodes.append(last_accessable_node)
            # if not found and curr_node + 6 not in visited_nodes and curr_node + 6 < n*n:
            #     queue.append((last_accessable_node, curr_node, distance + 1))
            # print(queue)
            print(queue)
            # break
        return -1
