class Solution:
    def build_adjacency_list(self, edges: List[List[int]], n: int) -> defaultdict:
        """Builds an adjacency list representation of an undirected graph."""
        edge_map = defaultdict(list)
        for start, end in edges:
            edge_map[start].append(end)
            edge_map[end].append(start)
        return edge_map

    def count_reachable_nodes(self, edge_map: defaultdict, n: int, k: int, depth_increment: int = 1) -> List[int]:
        """Counts nodes reachable within k steps from each node in the graph."""
        result = [0] * n
        for start_node in range(n):
            queue = deque([(start_node, 0)])
            not_visited = [True] * n
            while queue:
                curr_node, depth = queue.popleft()
                result[start_node] += int(depth <= k)
                not_visited[curr_node] = False
                for adj_node in edge_map[curr_node]:
                    if depth + depth_increment <= k and not_visited[adj_node]:
                        queue.append((adj_node, depth + depth_increment))
        return result

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """Computes the maximum number of target nodes reachable by combining two trees."""
        # Get number of nodes in each tree
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # Build adjacency lists for both trees
        edge_map1 = self.build_adjacency_list(edges1, n)
        edge_map2 = self.build_adjacency_list(edges2, m)
        
        # Compute reachable nodes for first tree with depth k
        first_tree_ans = self.count_reachable_nodes(edge_map1, n, k, 1)
        
        # Compute max reachable nodes for second tree with depth k-1
        max_ans = 0
        for start_node in range(m):
            queue = deque([(start_node, 0)])
            not_visited = [True] * m
            ans = 0
            while queue:
                curr_node, depth = queue.popleft()
                ans += int(depth <= k - 1)
                not_visited[curr_node] = False
                for adj_node in edge_map2[curr_node]:
                    if depth + 2 <= k and not_visited[adj_node]:
                        queue.append((adj_node, depth + 1))
            max_ans = max(ans, max_ans)
        
        # Combine results
        return [i + max_ans for i in first_tree_ans]