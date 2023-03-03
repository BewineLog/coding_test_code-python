import sys

sys.setrecursionlimit(1000000)
def search(maps,row,column,visited,value):
    if (row,column) in visited or 0 > row or row > len(maps) -1 or column < 0 or column > len(maps[0]) -1 or maps[row][column] == 'X':
        return value
    value += int(maps[row][column])
    visited.append((row,column))
    value = search(maps,row-1,column,visited,value)
    value = search(maps,row+1,column,visited,value)
    value = search(maps,row,column-1,visited,value)
    value = search(maps,row,column+1,visited,value)
    
    return value

def solution(maps):
    answer = []
    visited = []
    maps = [list(Amap) for Amap in maps]
    value = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X' or (i,j) in visited:
                continue
            answer.append(search(maps,i,j,visited,value))

    
    return sorted(answer) if answer else [-1]
