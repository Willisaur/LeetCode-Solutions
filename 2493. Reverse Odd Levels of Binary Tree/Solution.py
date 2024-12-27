# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        
        while stack and stack[0].left:
            # reverse child layer and grandchild layer (to undo reversing lower levels)
            children = []
            grandchildren = []
            for node in stack:
                if node.left.left:
                    grandchildren.append(node.left.left)
                    grandchildren.append(node.left.right)
                    grandchildren.append(node.right.left)
                    grandchildren.append(node.right.right)
                children.append(node.left)
                children.append(node.right)
            # do swaps
            for i in range(len(stack)):
                stack[i].left = children.pop()
                stack[i].right = children.pop()

                if stack[i].left.left:
                    stack[i].left.left = grandchildren[i*4]
                    stack[i].left.right = grandchildren[i*4 + 1]
                    stack[i].right.left = grandchildren[i*4 + 2]
                    stack[i].right.right = grandchildren[i*4 + 3]
            # update q
            stack = grandchildren
        return root
