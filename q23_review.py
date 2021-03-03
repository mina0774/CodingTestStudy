# 정렬 문제 - 국영수 (백준 10825)

# N명의 이름, 국어, 영어, 수학 점수
# 1) 국어 점수 감소 순
# 2) 영어 점수 증가 순
# 3) 수학 점수 감소 순
# 4) 이름 사전 순

n=int(input())

students=[]
for _ in range(n):
    students.append(list(map(str,input().split())))

students.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in students:
    print(student[0])