#stack
import sys

while(True):
    i = sys.stdin.readline()
    stack = []

    if(i =='.\n'):
        break
    if((i.count('(') != i.count(')') )or(i.count('[') != i.count(']')) ): #괄호 갯수가 안맞으면 확인할 필요없이 no
        print('no')
        continue
    if(i.count('(')==i.count(')')==i.count('[')==i.count(']')==0): #괄호가 없으면 무조건 yes
        print('yes')
        continue

    for a in i:
        if (a not in '()[]'):
            continue
        if(a == '(' or a == '['):
            stack.append(a)
        elif(a == ']'):
            if(len(stack) != 0 and stack[-1] == '['):
                stack.pop()
            else:
                stack.append(a)
                break
        elif(a== ')'):
            if (len(stack) != 0 and stack[-1] == '('):
                stack.pop()
            else:
                stack.append(a)
                break
    if(len(stack) == 0):
        print('yes')
    else:
        print('no')

