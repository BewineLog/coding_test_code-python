import sys
from collections import deque

def push (q:deque,val:int):
    q.append(val)
def pop(q:deque):
    if q.__len__() == 0:
        print('-1')
    else:
        print(q.popleft())
def size(q:deque):
    print(q.__len__())

def empty(q:deque):
    if q.__len__():
        print('0')
    else:
        print('1')

def front(q:deque):
    if q.__len__():
        t = q.popleft()
        print(t)
        q.appendleft(t)
    else:
        print('-1')

def back(q:deque):
    if q.__len__():
        t = q.pop()
        print(t)
        q.append(t)
    else:
        print('-1')


n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(q, command[1])
    elif command[0] == 'pop':
        pop(q)
    elif command[0] == 'size':
        size(q)
    elif command[0] == 'empty':
        empty(q)
    elif command[0] == 'front':
        front(q)
    elif command[0] == 'back':
        back(q)
