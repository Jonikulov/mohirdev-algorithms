class Stack:
    def __init__(self,place):
        self.stack = []
        # assigning how many spaces the stack's going to take
        self.place = place

    def push(self,data):
        """adding element"""
        if self.place!=0:
            self.stack.insert(0,data)
            # one element added -> one space filled
            self.place -= 1
        else:
            return "the stack is full"

    def pop(self,item):
        """pop out the element"""
        for i in range(len(self.stack)):
            if item==self.stack[i]:
                # one element pulled out -> one empty space
                self.place += 1
                return self.stack.pop(i)

    def isEmpty(self):
        """checking if the stack is empty"""
        if self.stack:
            return False
        else:
            return True

    def isFull(self):
        """checking if the stack is full"""
        if self.place==0:
            return "the stack is full"
        else:
            return "the stack is not full"

    def peek(self):
        """showing the last added item in stack"""
        return self.stack[0]

obj1 = Stack(5)

obj1.push(1)
obj1.push(2)
obj1.push(3)

print(obj1.peek())