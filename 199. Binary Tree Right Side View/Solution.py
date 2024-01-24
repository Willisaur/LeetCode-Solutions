# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root] if root else []
        nextQueue = []
        result = [root.val] if root else []
        while queue:
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            if nextQueue:
                result.append(nextQueue[-1].val)
            queue = nextQueue
            nextQueue = []
        return result