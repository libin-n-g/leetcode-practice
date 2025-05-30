class Solution:
    def build_adjacency_list(self, edges: List[List[int]]) -> defaultdict:
        """Builds an adjacency list representation of an undirected graph."""
        edge_map = defaultdict(list)
        for start, end in edges:
            edge_map[start].append(end)
            edge_map[end].append(start)
        return edge_map

    def count_reachable_nodes(self, edge_map: defaultdict, n: int, k: int) -> List[int]:
        """Counts nodes reachable within k steps from each node in the graph."""
        result = [0] * n
        for start_node in range(n):
            queue = deque([(start_node, 0, -1)])
            while queue:
                curr_node, depth, parent = queue.popleft()
                result[start_node] += 1
                for adj_node in edge_map[curr_node]:
                    if depth == k:
                        break
                    if adj_node != parent:
                        queue.append((adj_node, depth + 1, curr_node))
        return result

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """Computes the maximum number of target nodes reachable by combining two trees."""
        # Get number of nodes in each tree
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        # Build adjacency lists for both trees
        edge_map1 = self.build_adjacency_list(edges1)
        edge_map2 = self.build_adjacency_list(edges2)
        
        # Compute reachable nodes for first tree with depth k
        first_tree_ans = self.count_reachable_nodes(edge_map1, n, k)

        if k == 0: return first_tree_ans
        # Compute max reachable nodes for second tree with depth k-1
        max_ans = 0
        for start_node in range(m):
            queue = deque([(start_node, 0, -1)])
            ans = 0
            while queue:
                curr_node, depth, parent = queue.popleft()
                ans += 1
                for adj_node in edge_map2[curr_node]:
                    if depth + 1 == k:
                        break
                    if adj_node != parent:
                        queue.append((adj_node, depth + 1, curr_node))
            max_ans = max(ans, max_ans)
        
        # Combine results
        return [i + max_ans for i in first_tree_ans]