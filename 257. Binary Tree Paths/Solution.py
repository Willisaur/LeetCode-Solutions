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
        if self.isLeaf(node):
            paths.append(currentPath)
            return
        if node.left:
            self.findSolutions(node.left, f"{currentPath}->{str(node.left.val)}", paths)
        if node.right:
            self.findSolutions(node.right, f"{currentPath}->{str(node.right.val)}", paths)
        return
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        self.findSolutions(root, f"{root.val}", paths)
        return paths
        