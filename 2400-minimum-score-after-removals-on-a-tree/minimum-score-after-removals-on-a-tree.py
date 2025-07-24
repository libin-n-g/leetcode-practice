class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        N = len(nums)
        edges_map = defaultdict(list)
        for s, e in edges:
            edges_map[s].append(e)
            edges_map[e].append(s)
        
        xor_sum_tree = [0]*N
        def calculate_xor_sum(node, parent):
            current_sum = nums[node]
            for t in edges_map[node]:
                if t != parent:
                    current_sum ^= calculate_xor_sum(t, node)
            xor_sum_tree[node] = current_sum
            return current_sum
        calculate_xor_sum(0, -1)

        tree_nodes = [0] * N
        def add_tree_nodes(node, parent):
            tree_nodes[node] = set([node])
            for t in edges_map[node]:
                if t != parent:
                    tree_nodes[node] |= add_tree_nodes(t, node)
            return tree_nodes[node]
        
        add_tree_nodes(0, 0)
        # Now we consider 2 cases. Let o be tree rooted at 0, i be tree rooted at i and j be tree routed at j
        # 1. If o, i, j are not contained in eachother (assuming we romioved edge from x to i and x_dash to j).
        # 2. If j is contained in i tree. (vise versa) (before removing the corresponding edge)
        best = float('inf')
        for i in range(1, N):
            for j in range(i+1, N):
                if i in  tree_nodes[j]:
                    tree_o = xor_sum_tree[0] ^ xor_sum_tree[j]
                    tree_i = xor_sum_tree[i]
                    tree_j = xor_sum_tree[j] ^ xor_sum_tree[i] # XOR will cancell the first addition in big tree_j
                elif j in tree_nodes[i]:
                    tree_o = xor_sum_tree[0] ^ xor_sum_tree[i]
                    tree_i = xor_sum_tree[i] ^ xor_sum_tree[j] 
                    tree_j = xor_sum_tree[j]
                else:
                    tree_o = xor_sum_tree[0] ^  xor_sum_tree[i] ^ xor_sum_tree[j]
                    tree_j = xor_sum_tree[j]
                    tree_i = xor_sum_tree[i]
                best = min(best, max(tree_o, tree_i, tree_j) - min(tree_o, tree_i, tree_j))
        return best