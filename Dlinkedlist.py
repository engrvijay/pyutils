class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    def InsertAtStart(self, data):
        new_ele = Node(data)
        new_ele.next = self.head
        if self.head is not None:
            new_ele.prev = self.head
        self.head = new_ele

    def InsertAtEnd(self, data):
        new_ele = Node(data)
        if self.head is None:
            new_ele.next = self.head
            self.head = new_ele
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            new_ele.prev = temp
            temp.next = new_ele

    def InsertAt(self, data, preNode):
        if preNode is None:
            return
        new_ele = Node(data)
        new_ele.next = preNode.next
        preNode.next = new_ele
        new_ele.prev = preNode
        if new_ele.next is not None:
            new_ele.next.prev = new_ele

    def printList(self):
        temp = self.head
        print("start printing")
        while temp:
            print(temp.data, end=' ')  # Print the data in the current node
            temp = temp.next  # Move to the next node
            print()  # Ensures the output is followed by a new line

    def enumerate(self):
        current = self.head
        while current is not None:
            # Passing values with yield makes this a generator.
            yield current
            current = current.next

    def find(self, val):
        temp = self.head
        print("start find")
        while temp:
            if temp.data == val:
                return temp  # if found returned the current node
            temp = temp.next  # Move to the next node


if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()
    llist.InsertAtStart('fox')
    llist.InsertAtStart('brown')
    llist.InsertAtStart('quick')
    llist.InsertAtStart('the')
    llist.printList()
    llist.InsertAtEnd('jumps')
    llist.printList()
    llist.InsertAtEnd('down')
    llist.printList()

    item = llist.find("jumps")
    if item is not None:
        print("found data:", item.data)

for node in llist.enumerate():
    print("Node data:", node.data)
