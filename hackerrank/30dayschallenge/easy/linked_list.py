def insert(self,head,data): 
#Complete this method
    if(head == None):
        head = Node(data)
    else:
        current = head
        while current:
            if(current.next == None):
                current.next = Node(data)
                break
            else:
                current = current.next
    return head