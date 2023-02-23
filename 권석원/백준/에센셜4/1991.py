import sys

N = int(sys.stdin.readline())

tree = {}

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def pre_search(node):
    print(node.value,end='')

    if node.left != None:
        pre_search(tree[node.left])
    if node.right != None:
        pre_search(tree[node.right])

def mid_search(node):
    
    if node.left != None:
        mid_search(tree[node.left])
    
    print(node.value,end='')

    if node.right != None:
        mid_search(tree[node.right])

def post_search(node):
    if node.left != None:
        post_search(tree[node.left])
    if node.right != None:
        post_search(tree[node.right])

    print(node.value,end='')


for _ in range(N):
    root, left, right = sys.stdin.readline().rstrip().split()

    node = Node(root)

    if left != '.':
        node.left = left
    if right != '.':
        node.right = right

    tree[root] = node

pre_search(tree['A'])
print()
mid_search(tree['A'])
print()
post_search(tree['A'])



