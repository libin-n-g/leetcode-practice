class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        visited_node = [{}, {}]
        queue = deque([(node1, 0, 1, 0), (node2, 1, 0, 0)])
        ret = n
        min_max_distance = n
        while queue:
            curr_node, visited_node_index1, visited_node_index2, distance = queue.popleft()
            visited_node[visited_node_index1][curr_node] = distance
            if curr_node in visited_node[visited_node_index2]:
                curr_max_distance = max(visited_node[0][curr_node], visited_node[1][curr_node])
                if min_max_distance >= curr_max_distance:
                    min_max_distance = curr_max_distance
                    ret = min(ret, curr_node)
            if edges[curr_node] != -1 and edges[curr_node] not in visited_node[visited_node_index1]:
                queue.append((edges[curr_node], visited_node_index1, visited_node_index2, distance+1))
        return ret if ret != n else -1 