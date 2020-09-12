class Node(object):

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

nodes = []
in_res = []
pre_res = []

def insert(node):

    def compare(p):
        if p.key > node.key:
            if p.left:
                compare(p.left)
            else:
                p.left = node
        else:
            if p.right:
                compare(p.right)
            else:
                p.right = node

    if len(nodes):
        p = nodes[0]
        compare(p)
    else:
        nodes.append(node)

def find(key):
    p = nodes[0]

    while True:
        if p is None:
            print('no')
            return
        if p.key > key:
            p = p.left
        elif p.key < key:
            p = p.right
        else:
            print('yes')
            return

def inorder(node):
    if node.left:
        inorder(node.left)
    in_res.append(node.key)
    if node.right:
        inorder(node.right)

def preorder(node):
    pre_res.append(node.key)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def main():
    n = int(input())
    for i in range(n):
        inp = input().split()

        if len(inp) == 2:
            num = int(inp[1])
            if inp[0] == 'insert':
                node = Node(int(num))
                insert(node)
            elif inp[0] == 'find':
                find(num)

        elif len(inp) == 1:
           if len(nodes):
               root = nodes[0]
               in_res.clear()
               pre_res.clear()
               inorder(root)
               preorder(root)
               print(' ', end='')
               print(' '.join(map(str, in_res)))
               print(' ', end='')
               print(' '.join(map(str, pre_res)))

           else:
               print('')


if __name__ == '__main__':
    main()
