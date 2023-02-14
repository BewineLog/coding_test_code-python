def change_to_days(today):
    y,m,d = map(int,today.split('.'))
    
    return 28*12*y + 28*m + d
def solution(today, terms, privacies):
    answer = []
    termdic = {i[0]:28*int(i[2:]) for i in terms}
    today = change_to_days(today)
    
    for num,i in enumerate(privacies):
        date = change_to_days(i.split(' ')[0]) + termdic[i.split(' ')[1]]
        if today >= date :
            answer.append(num+1)
    
    
    return answer
