# Implementing a Stack using List in very easy as the List Data Structure is already present in Python.
# Stack is a Data Structure which will put a New Item on the top and delete a recently added element to List.
# Stack works on FIFO concept: First in First Out. 

# Initializing a Stack
stack = [1,2,3,4,5,6,7]
#        ^           ^
#        |           |
#   First Element    |
#                Last Element(Recently Added)
print(stack)
print('**************************************')

# Adding an element to List
stack.append(8)
print(stack)
print('**************************************')

# Removing an element from Stack
# If the list is empty then IndexError is raised : 'IndexError: pop from empty list'
try:
    stack.pop()
except IndexError as e:
    print("Exception Occurred: " + str(e))
finally:
    print(stack)
    print('**************************************')
    
