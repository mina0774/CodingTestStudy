# 만들 수 없는 금액

# 그리디를 이용 - 아직 잘 모르겠어.. 이해가 안가
n=int(input())
array=list(map(int,input().split()))
array.sort()
target=1

for i in array:
    if target<i:
        break
    target+=i

print(target)