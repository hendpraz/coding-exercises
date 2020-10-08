# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def listPrinter(head):
            node = head
            while node != None:
                print(node.val)
                node = node.next
            
        node = head
        count_node = 0
        while node != None:
            node = node.next
            count_node += 1
        
        if count_node == 0:
            return head
        else:
            k = k % count_node

            if k == 0:
                return head
            else:
                new_head = head
                prev_node = None

                j = count_node - k
                while j > 0:
                    prev_node = new_head
                    new_head = new_head.next
                    j -= 1

                prev_node.next = None

                tail = new_head
                while tail.next != None:
                    tail = tail.next

                tail.next = head

                # listPrinter(new_head)

                return new_head
            
