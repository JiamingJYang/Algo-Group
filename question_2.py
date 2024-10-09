class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class IntStack:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top     # new node links to the current top
        self.top = new_node          # new node now becomes the top 
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_value = self.top.value    # current top gets popped. save its value
        self.top = self.top.next         # top now becomes the next in stack
        self._size -= 1
        return popped_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.value
    
    def size(self):
        return self.size
    
    #Reference: My own code from CMSC 141 and 142 projects