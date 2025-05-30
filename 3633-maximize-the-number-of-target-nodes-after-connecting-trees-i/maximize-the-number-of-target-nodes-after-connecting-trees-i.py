class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        edge_map1 = defaultdict(list)
        for s, e in edges1:
           edge_map1[s].append(e)
           edge_map1[e].append(s)
        edge_map2 = defaultdict(list)
        for s, e in edges2:
           edge_map2[s].append(e)
           edge_map2[e].append(s)
        queue = deque()
        first_tree_ans = [0]*n
        for i in range(n):
            depth = 0
            queue.append((i, 0))
            not_visited = [True]*n
            while queue:
                curr_node, depth = queue.popleft()
                if depth <= k: 
                    first_tree_ans[i] += 1
                not_visited[curr_node] = False
                for adj_node in edge_map1[curr_node]:
                    if depth + 1 <= k and not_visited[adj_node]:
                        queue.append((adj_node, depth + 1))
        # print(first_tree_ans)
        max_ans = 0
        for i in range(m):
            depth = 0
            queue.append((i, 0))
            not_visited = [True]*m
            ans = 0
            while queue:
                curr_node, depth = queue.popleft()
                if depth <= k-1:
                    ans += 1
                not_visited[curr_node] = False
                for adj_node in edge_map2[curr_node]:
                    if depth + 2 <= k and not_visited[adj_node]:
                        queue.append((adj_node, depth + 1))
            max_ans = max(ans, max_ans)
        return [i+ max_ans for i in first_tree_ans]