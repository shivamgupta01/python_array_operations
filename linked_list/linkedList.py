import node
class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def return_size(self):
        return "The Size for the Linked List is : " + str(self.size)

    def insert_start(self,data):
        newNode = node.Node(data)
        self.size = self.size + 1
        if self.head == None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    def insert_end(self,data):
        self.size = self.size + 1
        newNode = node.Node(data)
        if self.size == 1:
            self.head = newNode
        else:
            pntr = self.head
            while(pntr.nextNode!=None):
                pntr = pntr.nextNode
            pntr.nextNode = newNode
    
    def remove_node(self,data):
        pntr = self.head
        counter = 1
        flag = False
        if pntr == None:
            print('The LinkedList is empty')
        elif pntr.data == data:
            self.head = self.head.nextNode
            print('The Data removed at counter: 0')
            flag = True
            counter =+1
            self.size = self.size - 1
        else: 
            while pntr.nextNode != None:
                if pntr.nextNode.data == data:
                    print('The Data removed at counter: ' + str(counter))
                    pntr.nextNode = pntr.nextNode.nextNode
                    flag = True
                    self.size = self.size - 1
                    break
                counter = counter + 1
                pntr = pntr.nextNode
        if flag != True:
            print('The Data Node is not found in the LinkedList')

    def print_nodes(self):
        pntr = self.head
        if self.size == 0:
            print("No Nodes in Linked List")
        else:
            while (pntr!=None):
                print(pntr.data)
                pntr = pntr.nextNode
            print('Size of LinkedList = ' + str(self.size))

if __name__ == '__main__':
    s = LinkedList()
    # s.insert_end(1)
    # s.insert_end(2)
    s.insert_end(3)
    s.insert_end(4)
    s.print_nodes()
    s.remove_node(4)
    s.print_nodes()

    print(s.return_size())