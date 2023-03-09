def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda x: (x[col-1],-x[0]))
    seq = []
    for i in range(row_begin-1,row_end):
        s = 0
        for val in data[i]:
            s += val % (i+1)
        seq.append(s)
    
    answer = seq[0]
    for i in range(1,len(seq)):
        answer = answer ^ seq[i]
    return answer
