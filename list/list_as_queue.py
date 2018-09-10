# Implementing List as Queue.
#
# While deleting first element from List the whole list is shuffled, 
# hence we will use python collections Module.

# Deque can be used to pop elements from both the ends from a list
from collections import deque
queue = deque(['one','two','three'])
queue.append('four')
queue.append('five')

# Pop left item.
print(queue.popleft())
print('*****************************')
print(queue.popleft())  
print('*****************************')
print(queue)
print('*****************************')
