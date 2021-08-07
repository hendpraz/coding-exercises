"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.res = dict()
        self.process(root, 0)
        
        final_res = []
        for key in self.res:
            final_res.append(self.res[key])
        
        return final_res
        
    def process(self, node: 'Node', level: int):
        if node:
            if level not in self.res:
                self.res[level] = []

            self.res[level].append(node.val)

            for child in node.children:
                self.process(child, level + 1)