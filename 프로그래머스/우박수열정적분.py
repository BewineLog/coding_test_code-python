# (앞의 좌표 + 뒤의 좌표 /2) 넓이가 나옴
def func(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2 
    A = (y2-y1)/(x2-x1)

    return (A/2 * (x2**2 - x1**2) + (y2 - A*x2)*(x2-x1))
    
    
def solution(k, ranges):
    answer = []
    pos = [(0,k)]
    integral =[]
    
    while k != 1:
        k = k //2 if k % 2 ==0 else k*3 + 1
        pos.append((pos[-1][0]+1,k))
        
    #한칸 구간별 적분 결과 구하기
    for idx in range(0,len(pos)-1):
        integral.append(func(pos[idx],pos[idx+1]))
    length = len(integral)
    for a,b in ranges:
        if -b > length-a :
            answer.append(-1)
        else:
            answer.append(sum(integral[a:length + b]))
    
    return answer
