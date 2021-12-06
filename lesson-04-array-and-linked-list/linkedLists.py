# Making To-Do list with Linked Lists
"""
Sample To-Do List:
- Work-out
- Reading
- Classes
- Cycling
- Courses
- Practice coding
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def push(self,key):
        """adding node to head of the list"""
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev,key):
        """inserting a new node after previous node"""
        if prev==None:
            print("previous node not found")
            return
        new_node = Node(key)
        new_node.next = prev.next
        prev.next = new_node

    def append(self,key):
        """adding node to the end of the list"""
        new_node = Node(key)
        if self.head==None:
            self.head = new_node
            return
        tmp = self.head
        while tmp:
            prev = tmp
            tmp = tmp.next
        prev.next = new_node
        tmp = new_node

    def deleteNode(self,key):
        """deleting node from list"""
        tmp = self.head
        if tmp.data==key:
            self.head = tmp.next
            tmp = None
            return

        while tmp:
            if tmp.data!=key:
                prev = tmp
                tmp = tmp.next
            else:
                break

        if tmp==None:
            return
        prev.next = tmp.next
        tmp = None            


# creating a new linked list
llist = LinkedList()

# assigning nodes
llist.head = Node("work-out")
read = Node("reading")
classes = Node("classes")
cycle = Node("cycling")
study = Node("courses")
practice = Node("coding")

# linking nodes
llist.head.next = read
read.next = classes
classes.next = cycle
cycle.next = study
study.next = practice

# print(llist.head.data)
# print(llist.head.next.data)
# print(read.next.data)

llist.printList()
print()

# llist.push('running')
# llist.printList()

# llist.insertAfter(llist.head.next,'science')
# llist.printList()

# llist.append('maths')
# llist.printList()

llist.deleteNode('coding')
llist.printList()