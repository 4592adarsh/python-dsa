#------------List-------------

# creating a list 
A = [1,2,3]
print(A)

# Adding an element at the end 
A.append(4)
print(A)

# Delete an element from the end 
A.remove(4)
print(A)

# Random element delete 
#A.remove(2)   # in python a.remove() will remove the first occurrence of that element , use a.pop() to remove from an index

A.pop(2)
print(A)

# Insert a value at an index , needs index and value as input

A.insert(2,9)
print(A)

# Modifying an element 
A[1]=7
print(A)

A[0]=8
print(A)

# Random Access

print (A[0])
print (A[1])
# print (A[5])


#Check if a value is present or not 

if 6 in A:
    print(True)
else:
    print(False)
    
# Check length of list 

print(len(A))

#------------Strings-------------

s = "hello"
b = s + "z"
print (b)

# Check if an element is in the string 

if 'a' in s:
    print(True)
else:
    print(False)
    
# Access in position
print (s[2])

# check length

print (len(b))