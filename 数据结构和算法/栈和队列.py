class Stack(object):
    def __init__(self):
        self.item = []
    def is_empty(self):
        return self.item == []
    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item)-1]
    def size(self):
        return len(self.item)

class Queue(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)