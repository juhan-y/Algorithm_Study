n = int(input())
dic = dict()
for _ in range(n):
    a, b ,c = input().split()
    dic[a] = [b, c]

def preorder(start):
    print(start, end = '')
    if dic[start][0] != '.':
        preorder(dic[start][0])
    if dic[start][1] != '.':
        preorder(dic[start][1])
    
def inorder(start):
    if dic[start][0] != '.':
        inorder(dic[start][0])
    print(start, end = '')
    if dic[start][1] != '.':
        inorder(dic[start][1])

def postorder(start):
    if dic[start][0] != '.':
        postorder(dic[start][0])
    if dic[start][1] != '.':
        postorder(dic[start][1])
    print(start, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')