from collections import defaultdict
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # N is the number of nodes in the tree
        N = len(nums)
        
        # Create an adjacency list representation of the tree
        # edges_map[node] contains all neighbors of node
        edges_map = defaultdict(list)
        for s, e in edges:
            edges_map[s].append(e)
            edges_map[e].append(s)
        
        # Array to store XOR sum of each subtree rooted at node i
        xor_sum_tree = [0] * N
        
        # DFS to calculate XOR sum of each subtree
        def calculate_xor_sum(node, parent):
            # Start with the value of current node
            current_sum = nums[node]
            # Recursively calculate XOR for all children except parent
            for t in edges_map[node]:
                if t != parent:
                    current_sum ^= calculate_xor_sum(t, node)
            # Store the XOR sum for this subtree
            xor_sum_tree[node] = current_sum
            return current_sum
        
        # Calculate XOR sums starting from root (node 0)
        calculate_xor_sum(0, -1)

        # Array to store set of nodes in each subtree
        tree_nodes = [0] * N
        
        # DFS to build sets of nodes for each subtree
        def add_tree_nodes(node, parent):
            # Initialize set with current node
            tree_nodes[node] = set([node])
            # Add all nodes from children's subtrees
            for t in edges_map[node]:
                if t != parent:
                    tree_nodes[node] |= add_tree_nodes(t, node)
            return tree_nodes[node]
        
        # Build node sets starting from root
        add_tree_nodes(0, 0)
        
        # Initialize best score as infinity
        best = float('inf')
        
        # Try all possible pairs of edges to remove
        # This creates three components: tree_o (remaining tree), tree_i, tree_j
        for i in range(1, N):
            for j in range(i + 1, N):
                # Case 1: If node i is in subtree of j
                if i in tree_nodes[j]:
                    # tree_o: XOR of all nodes except subtree j
                    tree_o = xor_sum_tree[0] ^ xor_sum_tree[j]
                    # tree_i: XOR of subtree i
                    tree_i = xor_sum_tree[i]
                    # tree_j: XOR of subtree j excluding subtree i
                    tree_j = xor_sum_tree[j] ^ xor_sum_tree[i]
                # Case 2: If node j is in subtree of i
                elif j in tree_nodes[i]:
                    # tree_o: XOR of all nodes except subtree i
                    tree_o = xor_sum_tree[0] ^ xor_sum_tree[i]
                    # tree_i: XOR of subtree i excluding subtree j
                    tree_i = xor_sum_tree[i] ^ xor_sum_tree[j]
                    # tree_j: XOR of subtree j
                    tree_j = xor_sum_tree[j]
                # Case 3: If subtrees i and j are disjoint
                else:
                    # tree_o: XOR of all nodes except subtrees i and j
                    tree_o = xor_sum_tree[0] ^ xor_sum_tree[i] ^ xor_sum_tree[j]
                    # tree_i: XOR of subtree i
                    tree_i = xor_sum_tree[i]
                    # tree_j: XOR of subtree j
                    tree_j = xor_sum_tree[j]
                
                # Calculate score as max XOR - min XOR of the three components
                best = min(best, max(tree_o, tree_i, tree_j) - min(tree_o, tree_i, tree_j))
        
        return best