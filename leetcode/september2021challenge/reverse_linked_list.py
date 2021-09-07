# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursively(node, before):
            temp = node.next
            
            node.next = before
            before = node
            
            if temp == None:
                return node
            else:
                return recursively(temp, before)
        
        def iteratively(node):
            next_node = None

            while node != None:
                temp = node.next

                node.next = next_node
                next_node = node

                node = temp

            return next_node

        if head:
            return recursively(head, None)
            # return iteratively(head)
        else:
            return head
