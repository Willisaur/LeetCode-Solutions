# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        
        while q and q[0].left:
            # reverse child layer and grandchild layer (to undo reversing lower levels)
            q_c = deque([])
            q_gc = deque([])
            for node in q:
                if node.left.left:
                    q_gc.append(node.left.left)
                    q_gc.append(node.left.right)
                    q_gc.append(node.right.left)
                    q_gc.append(node.right.right)
                q_c.append(node.left)
                q_c.append(node.right)
            # do swaps
            q_size = len(q)
            q_gc_size = len(q_gc)
            for i in range(q_size):
                q[i].left = q_c.pop()
                q[i].right = q_c.pop()

                if q[i].left.left:
                    q[i].left.left = q_gc[i*4]
                    q[i].left.right = q_gc[i*4 + 1]
                    q[i].right.left = q_gc[i*4 + 2]
                    q[i].right.right = q_gc[i*4 + 3]
            # update q
            q = q_gc
        return root
