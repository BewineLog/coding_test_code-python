import sys
import string

n = int(input())
binaryTree = dict()
rootNode = 'A'
for _ in range(n):
    root,left,right = sys.stdin.readline().rstrip().split()
    binaryTree[root] = [left,right]

def preorderTraversal(node):
    if node != '.':
        print(node,end='')
        for newNode in binaryTree[node]:
            preorderTraversal(newNode)

def inorderTraversal(node):
    if node != '.':
        newNode1, newNode2 = binaryTree[node]
        inorderTraversal(newNode1)
        print(node,end='')
        inorderTraversal(newNode2)



def postorderTraversal(node):
    if node != '.':
        for newNode in binaryTree[node]:
            postorderTraversal(newNode)
        print(node,end='')

preorderTraversal('A')
print()
inorderTraversal('A')
print()
postorderTraversal('A')
