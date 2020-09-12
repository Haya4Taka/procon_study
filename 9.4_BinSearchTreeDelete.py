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

def delete(key):
    p = ''
    c = nodes[0]
    direction = None

    def get_most_left(node):
        while True:
            if node.left is None:
                return node
            else:
                node = node.left


    while True:
        nonlocal p, direction
        if c is None:
            return
        if c.key > key:
            p = c
            c = c.left
            direction = 'left'
        elif c.key < key:
            p = c
            c = c.right
            direction = 'right'
        else:
            if c.left is None and c.right is None:
                if direction == 'right':
                    p.right = None
                elif direction == 'left':
                    p.left = None
                else:
                    global nodes
                    nodes = []

            elif c.right:
                if c.left:
                    most_left_of_c_right = get_most_left(c.right)
                    most_left_of_c_right.left = c.left
                if direction == 'right':
                    p.right = c.right
                elif direction == 'left':
                    p.left = c.right
            elif c.left:
                if direction == 'right':
                    p.right = c.left
                elif direction == 'left':
                    p.left = c.left
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
            elif inp[0] == 'delete':
                delete(num)

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
