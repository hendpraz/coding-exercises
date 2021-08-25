# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        lowest_value = ((10 ** 4) + 1) * (-1)
        return self.explore(root,  lowest_value)
        
    def explore(self, node: TreeNode, currentMax: int) -> int:
        point = 0
        
        newMax = currentMax
        if node:
            if node.val >= currentMax:
                newMax = node.val
                point += 1
                
            point += self.explore(node.left, newMax)
            point += self.explore(node.right, newMax)
            
        return point