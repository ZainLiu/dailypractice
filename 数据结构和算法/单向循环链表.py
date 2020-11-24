class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SinCycLinkedList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head.next
        while cur != self.__head:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        l = []
        if self.is_empty():
            return l
        cur = self.__head
        while cur.next != self.__head:
            l.append(cur.item)
            cur = cur.next
        return l

    def tail(self):
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        return cur

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            tail = self.tail()
            tail.next = node
            node.next = self.__head
            self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        tail = self.tail()
        tail.next = node
        node.next = self.__head
    def insert(self,pos, item):
        if pos <= 0:
            self.add(item)
        if pos >= (self.length()-1):
            self.append(item)
        cur = self.__head
        count = 0
        node = Node(item)
        while count < (pos-1):
            cur = cur.next
            count += 1
        node.next = cur.next
        cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    pre.next = cur.next
                return
            else:
                pre =cur
                cur = cur.next
        if cur.item == item:
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False



