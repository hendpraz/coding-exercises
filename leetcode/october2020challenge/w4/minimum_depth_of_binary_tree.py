# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # (node, depth)
        self.queue = []
        
        def isLeaf(node: TreeNode):
            if node.left == None and node.right == None:
                return True
            
        if root == None:
            return 0
        else:
            self.queue.append((root, 1))
            maxLen = len(self.queue)
            
            i = 0
            while i < maxLen:
                node, depth = self.queue[i]
                if isLeaf(node):
                    return depth
                else:
                    if node.left != None:
                        self.queue.append((node.left, depth + 1))
                        maxLen += 1

                    if node.right != None:
                        self.queue.append((node.right, depth + 1))
                        maxLen += 1
                    
                    i += 1
                    
                
