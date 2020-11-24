class Node(object):
    def __init__(self, item):
        self.pre = None
        self.next = None
        self.item = item

class DLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        dict = []
        cur = self.__head
        while cur != None:
            dict.append(cur.item)
            cur = cur.next
        return dict

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            pre = None
            count = 0
            while cur != None:
                if count < (pos-1):
                    count+=1
                    cur = cur.next
                node.next = cur.next
                cur.next.pre = node
                cur.next = node
                node.pre = cur

    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        self.__head.pre =None
                else:
                    cur.pre.next = cur.next
                    if cur.next:
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next


