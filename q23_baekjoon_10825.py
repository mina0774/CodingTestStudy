# 정렬 - 국영수 백준 10825
n=int(input())
students=[]

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
정렬 기준
1) 두번째 원소를 기준으로 내림차순 정렬
2) 두번째 원소가 같으면, 세번째 원소를 기준으로 오름차순 정렬
3) 세번째 원소가 같으면, 네번째 원소를 기준으로 내림차순 정렬
4) 네번째 원소가 같으면, 첫번째 원소를 기준으로 오름차순 정렬 
'''

students.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])