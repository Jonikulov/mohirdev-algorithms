# Making To-Do list with Singly Linked Lists
"""
Sample To-Do List:
- Work-out
- Reading
- Classes
- Cycling
- Courses
- Practice coding
"""

from linkedLists import Node, LinkedList

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