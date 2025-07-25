# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # RECIRSIVE SOLUTION
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited_inorder = []
        def inorder(root):
            if root:
                inorder(root.left)
                visited_inorder.append(root)
                inorder(root.right)
        def create_BST(left, right):
            if left > right:
                return None
            mid = left + (right - left)//2
            root = visited_inorder[mid]
            root.left = create_BST(left, mid - 1)
            root.right = create_BST(mid + 1, right)
            return root
        inorder(root)
        return create_BST(0, len(visited_inorder) - 1)

    def balanceBST_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root)
                root = root.right
        # Creating new balanced Binary tree
        n = len(inorder)
        mid = n // 2
        root = inorder[mid]
        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n-1))
        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = left + (right - left)//2
                child = inorder[mid]
                if child.val <= parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child, left, mid - 1))
                q.append((child, mid + 1, right))
            else:
                parent.left = parent.right = None
        return root