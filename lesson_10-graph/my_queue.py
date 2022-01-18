class Queue:
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f"{self.queue}"

    def isEmpty(self):
        """checking if the queue is empty"""
        if self.queue:
            return False
        else:
            return True

    def append(self,item):
        """adds an element at the end of the list"""
        if type(item)==list:
            self.queue += item
        else:
            self.queue.append(item)

    def pop(self,index):
        """removes the element at the specified position"""
        return self.queue.pop(index)

    def popleft(self):
        """removes the first element of queue"""
        return self.queue.pop(0)

    def remove(self,element):
        """removes the first item with the specified value"""
        self.queue.remove(element)