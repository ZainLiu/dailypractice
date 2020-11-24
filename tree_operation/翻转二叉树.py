class BinTree(object):
    def __init__(self,lchild,rchild,elem):
        self.lchild = lchild
        self.rchild = rchild
        self.elem = elem
    def __str__(self):
        return self.elem

# 广度优先遍历树
def travel(rootNode):
    result = []
    if rootNode == None:
        print(result)
    stack = []
    stack.append(rootNode)
    while stack:
        node = stack.pop(0)
        result.append(node.elem)
        if node.lchild != None:
            stack.append(node.lchild)
        if node.rchild != None:
            stack.append(node.rchild)
    print(result)

def invertTree(rootNode):
    stack = []
    cur = rootNode
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.lchild
        cur=stack.pop()
        cur.lchild,cur.rchild = cur.rchild,cur.lchild
        cur = cur.lchild
    return rootNode

node1 = BinTree(None,None,1)
node3 = BinTree(None,None,3)
node6 = BinTree(None,None,6)
node9 = BinTree(None,None,9)
node2 = BinTree(node1,node3,2)
node7 = BinTree(node6,node9,7)
node4 = BinTree(node2,node7,4)
travel(node4)
node = invertTree(node4)
travel(node4)

