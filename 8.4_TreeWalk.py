class Node(object):

    def __init__(self, id=-1, right=-1, left=-1, parent=-1):
        self.id = id
        self.right = right
        self.left = left
        self.parent = parent


n = int(input())
nodes = [Node() for _ in range(n)]
porder = []
iorder = []
posorder = []

def m():
    for _ in range(n):
        id, left, right = map(int, input().split())
        nodes[id].id = id
        nodes[id].right, nodes[id].left = right, left
        if left != -1:
            nodes[left].parent = id
        if right != -1:
            nodes[right].parent = id

    root = list(filter(lambda n: n.parent == -1, nodes))[0]

    print("Preorder")
    preorder(root.id)
    print(' ' + ' '.join(map(str, porder)))
    print("Inorder")
    inorder(root.id)
    print(' ' + ' '.join(map(str, iorder)))
    print("Postorder")
    postorder(root.id)
    print(' ' + ' '.join(map(str, posorder)))


def preorder(id):
    if id == -1:
        return
    porder.append(id)
    node = nodes[id]
    preorder(node.left)
    preorder(node.right)

def inorder(id):
    if id == -1:
        return
    node = nodes[id]
    inorder(node.left)
    iorder.append(id)
    inorder(node.right)

def postorder(id):
    if id == -1:
        return
    node = nodes[id]
    postorder(node.left)
    postorder(node.right)
    posorder.append(id)

if __name__ == '__main__':
    m()
