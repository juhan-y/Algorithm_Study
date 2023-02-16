n = int(input())
dic = {}

cnt = 0
root = '.'
for _ in range(n):
    a, b, c = input().split()
    if cnt == 0:
        root = a
    cnt += 1
    dic[a] = [b,c]

def preorder(node):
    print(node, end='')
    b, c = dic[node]
    if b != '.':
        preorder(b)
    if c != '.':
        preorder(c)

def inorder(node):
    b, c = dic[node]
    if b != '.':
        inorder(b)
    print(node, end='')
    if c != '.':
        inorder(c)

def postorder(node):
    b, c = dic[node]
    if b != '.':
        postorder(b)
    if c != '.':
        postorder(c)
    print(node, end='')

preorder(root)
print()
inorder(root)
print()
postorder(root)