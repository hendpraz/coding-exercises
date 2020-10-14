# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def addAllElements(node):
            if node != None:
                self.result.append(node.val)
                if node.left != None:
                    addAllElements(node.left)
                if node.right != None:
                    addAllElements(node.right)
        
        self.result = []
        addAllElements(root1)
        addAllElements(root2)
        
        return sorted(self.result)
        