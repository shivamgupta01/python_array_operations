class Node:
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class doubly_linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_head(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
if __name__ == '__main__':
    doubly_linked = doubly_linked_list()
    doubly_linked.insert_head(1)
    doubly_linked.insert_head(2)
    doubly_linked.insert_head(3)
    print(doubly_linked.size)

    
        