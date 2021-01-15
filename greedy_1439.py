s=input()

# 문자열 s가 모두 0으로 바뀌는 경우의 횟수
count0=0
# 문자열 s가 모두 1로 바뀌는 경우의 횟수
count1=0

# 첫번째 원소부터 확인
if s[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0,count1))

