# ------------------------------------Doubly linked list----------------------------- 

class DoublyNode:
    def __init__ ( self, val, next=None, prev =None):
        self.val = val
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.val)
    
Head = Tail = DoublyNode(1)
print(Head )

# ------------------------------------Doubly linked list----------------------------- 

class DoublyNode:
    def __init__ ( self, val, next=None, prev =None):
        self.val = val
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.val)
    
Head = Tail = DoublyNode(1)
# print(Head)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print (" <-> ".join(elements))
    
display(Head)

# Insert at beginning - O(1)

def insert_at_beginning ( head, tail , val ):
    new_node = DoublyNode(val , next=head )
    head.prev = new_node
    return new_node, tail 

head, tail = insert_at_beginning( Head , Tail , 7 )

display(head)

# Insert at the end - O(1)

def insert_at_end ( head, tail , val ):
    new_node = DoublyNode(val , prev=tail )
    tail.next = new_node
    return new_node, tail 

head, tail = insert_at_end( Head , Tail , 9 )

display(head)