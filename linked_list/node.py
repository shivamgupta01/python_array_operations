# LinkedList are much more dynamic data structure than Array. 
# Can store different Data Structures.
# Can allocates needed memory dynamically. 
# Easy Implementation


# Waste Memory because of reference.
# No Index / Random Access.
# No Reverse References. 

class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None

       