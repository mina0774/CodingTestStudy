s=input()
result=[]
num=0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        num+=int(i)

result.sort()

if num!=0:
    result+=str(num)

# 리스트를 문자열로 변환하여 출력
print(''.join(result))

