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