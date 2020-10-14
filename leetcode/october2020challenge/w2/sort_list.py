# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getValue(el):
            return el.val
        
        arr = []
        node = head
        
        while node != None:
            arr.append(node)
            node = node.next
            
        if len(arr) == 0:
            return None
        
        arr = sorted(arr, key=getValue)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i].next = None
            else:
                arr[i].next = arr[i+1]
            
        return arr[0]
