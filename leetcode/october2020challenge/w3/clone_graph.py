"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        def createGraph(node, masterKey, graphDict):
            graphDict[masterKey] = []
            
            for neighbor in node.neighbors:
                graphDict[masterKey].append(neighbor.val)

                key = neighbor.val
                if key not in graphDict:            
                    createGraph(neighbor, key, graphDict)
                    
        graphDict = dict()
        masterKey = node.val
        
        createGraph(node, masterKey, graphDict)
        # print(graphDict)
        
        nodeCollection = dict()
        for key in graphDict.keys():
            nodeCollection[key] = Node(key)
            
        for key in nodeCollection.keys():
            for neighborKey in graphDict[key]:
                nodeCollection[key].neighbors.append(nodeCollection[neighborKey])
        
        return nodeCollection[masterKey]
