# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(node, val):
            if val > node.val:
                if node.right == None:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
            elif val < node.val:
                if node.left == None:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            else:
                print("Something is wrong!")
        
        if root == None:
            return TreeNode(val)
        
        insert(root, val)
        
        return root
