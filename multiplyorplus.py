data=input()
result=int(data[0])

for i in range(1,len(data)):
    num=int(data[i])

# 현재 숫자가 1보다 작을 경우, 결과값 수가 1보다 작을 경우
    if num<=1 or result<=1:
        result+=num
    else:
        result*=num
print(result)