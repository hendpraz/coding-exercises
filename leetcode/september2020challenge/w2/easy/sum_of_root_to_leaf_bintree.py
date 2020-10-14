# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def binaryToDecimal(binary):
            return int(binary, 2)
        
        def isChildless(node):
            return node.left == None and node.right == None
        
        def addToResult(node, current_str):
            if isChildless(node):
                self.result.append(current_str + str(node.val))
            else:
                if node.left != None:
                    addToResult(node.left, current_str + str(node.val))
                if node.right != None:
                    addToResult(node.right, current_str + str(node.val))
        
        self.result = []
        addToResult(root, '')
        
        for i in range(len(self.result)):
            self.result[i] = binaryToDecimal(self.result[i])
            
        return sum(self.result)