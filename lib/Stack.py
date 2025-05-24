class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items or []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            return None
        # Check if the stack is full
        self.items.append(item)

    def pop(self):
     if not self.items:
        return None  # Return None if stack is empty
     return self.items.pop()
    
    def peek(self):
        if not self.items:
            return None
        # Return the last item without removing it
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    

    def full(self):
        if self.full is None:
            return False
        return len(self.items) >= self.limit

    def search(self, target):
        # checks how far is the element in the stack
        # returns -1 if not found
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        else:
            return -1