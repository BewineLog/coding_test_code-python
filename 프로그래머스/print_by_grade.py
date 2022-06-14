"""
-성적이 낮은 순서로 학생 출력하기
-N명의 학생 정보
-학생 정보는 이름과 학생의 성적으로 구분
"""
n = int(input())
array=[] * n

for _ in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array.sort(key = lambda x:x[1])

for student in array:
    print(student[0])
