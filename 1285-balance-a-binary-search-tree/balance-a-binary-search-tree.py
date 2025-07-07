# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedToBST(self, nums: List[TreeNode]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
        root = nums[mid]
        q = deque()
        q.append((root, 0, mid-1))
        q.append((root, mid+1, n-1))
        while q:
            parent, left, right = q.popleft()
            if left <= right:
                mid = left + (right - left)//2
                child = nums[mid]
                child.left = child.right = None
                if child.val <= parent.val:
                    parent.left = child
                else:
                    parent.right = child
                q.append((child, left, mid - 1))
                q.append((child, mid + 1, right))
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        print(list(map(lambda x: x.val, inorder)))
        return self.sortedToBST(inorder)