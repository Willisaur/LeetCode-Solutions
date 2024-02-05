# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, node):
        return not (node.left or node.right)
    def findSolutions(self, node, currentPath, paths):
        # solution
        if self.isLeaf(node):
            paths.append(currentPath)
            return
        # look deeper; use a choice
        if node.left:
            self.findSolutions(node.left, f"{currentPath}->{node.left.val}", paths)
        # look deeper; use a choice
        if node.right:
            self.findSolutions(node.right, f"{currentPath}->{node.right.val}", paths)
        # go back
        return

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.findSolutions(root, f"{root.val}", paths)
        return paths