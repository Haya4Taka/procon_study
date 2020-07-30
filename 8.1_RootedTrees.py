class Node(object):
    def __init__(self, parent=-1, left=None, right=None, children=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.children = children
        self.depth = None


MAX = 100005

nodes = [None]*MAX
n = int(input())

def determine_type(node):
    if node.parent == -1:
        return 'root'
    elif node.left is None:
        return 'leaf'
    else:
        return 'internal node'

def print_node(i):
    node = nodes[i]
    node_type = determine_type(node)
    print(f'node {i}: parent = {node.parent}, depth = {node.depth}, {node_type}, {node.children}')

def set_depth(id=0, d=0):
    node = nodes[id]
    node.depth = d
    if node.right is not None:
        set_depth(id=node.right, d=d)
    if node.left is not None:
        set_depth(id=node.left, d=d+1)

for _ in range(n):
    id, next_num, *children = map(int, input().split())
    left = children[0] if children else None
    if nodes[id]:
        nodes[id].left = left
        nodes[id].children = children
    else:
        nodes[id] = Node(left=left, children=children)

    for i, c in enumerate(children):
        right = 0
        try:
            right = children[i+1]
        except IndexError:
            right = None
        if nodes[c]:
            nodes[c].parent = id
            nodes[c].right = right
        else:
            nodes[c] = Node(parent=id, right=right)

root = next(filter(lambda n: n.parent == -1, nodes))
index = nodes.index(root)
set_depth(index)

for i in range(n):
    print_node(i)
