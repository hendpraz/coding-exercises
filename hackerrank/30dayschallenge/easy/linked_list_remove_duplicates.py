def removeDuplicates(self,head):
    #Write your code here
    if(head != None):
        curr1 = head
        while(curr1 != None):
            curr2 = curr1.next
            bfr = curr1
            while(curr2 != None):
                if(curr2.data == curr1.data):
                    bfr.next = bfr.next.next
                    curr2 = bfr.next
                else:
                    bfr = curr2
                    curr2 = bfr.next
            curr1 = curr1.next
            # self.display(head)
            # print()
    return head