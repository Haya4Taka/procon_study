class Node(object):

    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1
        self.sibling = -1

    def __str__(self):
        return f'parent: {self.parent} \n'\
               f'left: {self.left} \n' \
               f'right: {self.right} \n' \
               f'sibling: {self.sibling} \n'

nodes = []

def set_depth(nodes, node, d=0):
    node.d = d
    if node.left != -1:
        set_depth(nodes, nodes[node.left], d+1)

    if node.right != -1:
        set_depth(nodes, nodes[node.right], d+1)

def set_height(nodes, node):
    l_h = 0
    r_h = 0
    if node.left != -1:
        l_h = set_height(nodes, nodes[node.left]) + 1

    if node.right != -1:
        r_h = set_height(nodes, nodes[node.right]) + 1

    node.h = max([l_h, r_h])

    return node.h


def m():
    n = int(input())
    nodes = [Node() for _ in range(n)]

    for _ in range(n):
        id, l, r = map(int, input().split())
        nodes[id].left = l
        nodes[id].right = r

        if l != -1:
            nodes[l].parent = id
            nodes[l].sibling = r

        if r != -1:
            nodes[r].parent = id
            nodes[r].sibling = l

        # print("node after \n", nodes[id])


    root = list(filter(lambda n: n.parent == -1, nodes))[0]
    set_height(nodes, root)
    set_depth(nodes, root)

    for index, node in enumerate(nodes):
        degree = 0
        if node.left != -1 and node.right != -1:
            degree = 2
        elif node.left != -1 or node.right != -1:
            degree = 1
        else:
            degree = 0
        node_type = ''
        if node.parent == -1:
            node_type = 'root'
        elif degree == 2 or degree == 1:
            node_type = 'internal node'
        elif degree == 0:
            node_type = 'leaf'
        print(f'node {index}: parent = {node.parent}, sibling = {node.sibling}, degree = {degree}, depth = {node.d}, height = {node.h}, {node_type}')


if __name__ == '__main__':
    m()