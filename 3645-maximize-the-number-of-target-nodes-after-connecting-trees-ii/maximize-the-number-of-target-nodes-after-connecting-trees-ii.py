from enum import Enum

class Condition(Enum):
    ODD = 1
    EVEN = 2
class Solution:
    def create_edge_map(self, edges):
        edges_map = defaultdict(list)
        for s, e in edges:
            edges_map[s].append(e)
            edges_map[e].append(s)
        return edges_map

    def breadth_first_search(self, n, edge_map, condition=Condition.EVEN):
        if n <= 2:
            return [1]*n if condition == Condition.EVEN else [n // 2]*n
        ans = [0]*n
        odd_group = []
        even_group = []
        queue = deque([(0, 0, -1)])
        while queue:
            curr_node, depth, parent = queue.popleft()
            if depth % 2 == 0:
                even_group.append(curr_node)
            else:
                odd_group.append(curr_node)
            for adj_node in edge_map[curr_node]:
                if adj_node != parent:
                    queue.append((adj_node, depth+1, curr_node))
        if condition == Condition.EVEN:
            odd_group_res = len(odd_group)
            even_group_res = len(even_group)
        else:
            odd_group_res =  len(even_group)
            even_group_res = len(odd_group)
        for i in odd_group:
            ans[i] = odd_group_res
        for i in even_group:
            ans[i] = even_group_res
        return ans

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        edges_map1 = self.create_edge_map(edges1)
        edges_map2 = self.create_edge_map(edges2)
        ans1 = self.breadth_first_search(n, edges_map1, Condition.EVEN)
        ans2 = self.breadth_first_search(m, edges_map2, Condition.ODD)
        # print(ans1, ans2)
        max_ans2 = max(ans2)
        return [i + max_ans2 for i in ans1]
