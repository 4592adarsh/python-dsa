# node definition

class DoubleNode:
    def __init__ ( self , val , next=None, prev=None):
        self.val = val
        self.next = next 
        self.prev = prev
        
    def __str__(self):
        return str(self.val)

# display nodes 

def display(head):
    curr=head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr=curr.next
    print(" <-> ".join(elements))
    
initial_head = initial_tail = DoubleNode(1)

display(initial_head)


#insert at the beginning 

def insert_beginning ( head, tail , val ):
    new_node = DoubleNode(val , next = head)

    if head:
        head.prev = new_node
    else:
        tail = new_node
    return new_node, tail 

head , tail = insert_beginning( initial_head, initial_tail , 7)

print(" current list: ")
display (head)

# insert at the end

def insert_end ( head, tail, val ):
    new_node = DoubleNode( val , prev = tail )
    if tail:
        tail.next = new_node
    else:
        tail = new_node
    return head, new_node

head, tail = insert_end (head, tail, 9)
    
display(head)