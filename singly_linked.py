# ------------------------------------singly linked list----------------------------- 


# initialize the class
class SingleLinked:
    def __init__ (self, val , next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)
    
# creating a node and giving it values 

Head = SingleLinked(1)
A = SingleLinked(3)
B = SingleLinked(5)
C = SingleLinked(7)

# Now connecting these nodes to each other 

A.next=Head
Head.next=B
B.next=C

# Traversing through these nodes now ------ TC O(n)

curr = A
while curr:
    print(curr)
    curr=curr.next
    
# disply these nodes in a better way 

def display (head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))    # what join does ? if we have a list [1,2,3] , join will print them as 123 , so if we add "' -> '" before , it will act as a glue and will print the values as 1->2->3

display(A)

# Search for a value in  a node 

def search (head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
        
    return False

print(search (A, 7))

 