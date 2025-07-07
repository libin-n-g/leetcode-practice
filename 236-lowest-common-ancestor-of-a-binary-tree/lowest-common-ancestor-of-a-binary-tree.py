# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = deque()
        ancesters = {}
        if root: 
            queue.append(root)
            ancesters[root] = None
        while queue:
            node = queue.popleft()
            if node.left:
                ancesters[node.left] = node
                queue.append(node.left)
            if node.right:
                ancesters[node.right] = node
                queue.append(node.right)
            if q in ancesters and p in ancesters:
                break
        # print(ancesters)
        node1, node2 = p, q
        while node1 != node2:
            node1 = ancesters[node1] if node1 else q
            node2 = ancesters[node2] if node2 else p
        return node1