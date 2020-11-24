# 节点
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def length(self):
        cur = self.__head
        count = 0
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        items = []
        while cur != None:
            items.append(cur.item)
            cur = cur.next
        return items
    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur != Node:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            node = Node(item)
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        cur = self.__head
        while cur != None:
            if cur.nex.item != item:
                cur = cur.next
            else:
                cur.next = cur.next.next
                break
    def search(self,item):
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False






