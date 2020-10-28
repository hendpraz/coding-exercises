# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        else:
            listDict = dict()
            
            node = head
            while node != None:
                key = node.val
                if key in listDict:
                    for savedNode in listDict[key]:
                        if node == savedNode:
                            return node
                else:
                    listDict[key] = []
                    
                listDict[key].append(node)
                    
                node = node.next
                    
            return None
