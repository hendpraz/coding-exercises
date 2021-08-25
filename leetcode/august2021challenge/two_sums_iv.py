# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(node, k):
            if node and not self.found:
                target = k - node.val
                
                if target in self.num:
                    self.found = True
                else:
                    self.num.add(node.val)
                    find(node.left, k)
                    find(node.right, k)
                    
        self.num = set()
        self.found = False
        
        find(root, k)
        
        return self.found