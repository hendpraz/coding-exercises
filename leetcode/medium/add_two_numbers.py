# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            root = ListNode( (l1.val + l2.val) % 10 )
            node = root
            trailing_one = ( l1.val + l2.val ) // 10
            
            l1 = l1.next
            l2 = l2.next
            while l1 != None and l2 != None:
                node.next = ListNode( (l1.val + l2.val + trailing_one) % 10 )
                node = node.next
                
                trailing_one = ( l1.val + l2.val + trailing_one) // 10
            
                l1 = l1.next
                l2 = l2.next
                
            while l1 != None:
                node.next = ListNode((l1.val + trailing_one) % 10)
                node = node.next
                
                trailing_one = (l1.val + trailing_one) // 10
                
                l1 = l1.next
                
            while l2 != None:
                node.next = ListNode((l2.val + trailing_one) % 10)
                node = node.next
                
                trailing_one = (l2.val + trailing_one) // 10
                
                l2 = l2.next
                
            if trailing_one == 1:
                node.next = ListNode(1)
                
            return root