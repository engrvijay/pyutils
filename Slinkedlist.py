# Node Structure: A node in a linked list typically consists of two components:
# Data: It holds the actual value or data associated with the node.
# Next Pointer: It stores the memory address (reference) of the next node in the sequence.
# Head and Tail: The linked list is accessed through the head node, which points to the first node in the list.
# The last node in the list points to NULL or nullptr, indicating the end of the list. This node is known as the tail node.

# WHY
# Dynamic Data structure: The size of memory can be allocated or de-allocated at run time based on the operation insertion or deletion.
# Ease of Insertion/Deletion: The insertion and deletion of elements are simpler than arrays since no elements need to be shifted after insertion and deletion,
# Just the address needed to be updated.
# Efficient Memory Utilization: As we know Linked List is a dynamic data structure the size increases
# or decreases as per the requirement so this avoids the wastage of memory.
# Implementation: Various advanced data structures can be implemented using a linked list like a stack, queue, graph, hash maps, etc.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None
        self.tail = None  # Initialize head as None

    def InsertAtStart(self, data):
        new_ele = Node(data)
        if self.head is None:
            self.tail = new_ele

        new_ele.next = self.head
        self.head = new_ele

    def InsertAtEnd(self, data):
        new_ele = Node(data)
        if self.head is None:
            new_ele.next = self.head
            self.head = new_ele
            self.tail = new_ele
        else:
            self.tail.next = new_ele
            self.tail = new_ele

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
    print("found data:", item.data)

for node in llist.enumerate():
    print("Node data:", node.data)
