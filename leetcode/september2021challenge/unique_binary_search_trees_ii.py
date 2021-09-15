# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def gen(start, end):
            li = []
            
            if (start > end):
                li.append(None)
                return li
            
            if (start == end):
                li.append(TreeNode(start))
                return li
            
            for i in range(start, end + 1):
                leftPossibleTrees = gen(start, i - 1)
                rightPossibleTrees = gen(i+1, end)
                
                for lRoot in leftPossibleTrees:
                    for rRoot in rightPossibleTrees:
                        root = TreeNode(i)
                        root.left = lRoot
                        root.right = rRoot
                        li.append(root)
                        
            return li
        
        if n == 1:
            return [TreeNode(1)]
        else:
            return gen(1, n)
            
            
