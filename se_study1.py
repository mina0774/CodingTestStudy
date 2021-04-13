# 보물상자 비밀번호
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리
for test_case in range(1, T + 1):

    n, k = map(int, input().split())
    string=list(input())

    # 보물상자 한 변에 들어가는 숫자의 자릿수
    r=n//4

    result=[]
    # 한 변에 들어가있는 숫자 갯수만큼 반복한 후에는 처음과 같은 상태
    for i in range(r):
        for j in range(0,len(string),r):
            # 슬라이싱을 해서 결과에 없을 경우에만 추가
            if string[j:j+r] not in result:
                result.append(string[j:j+r])
        # 배열의 맨 뒤 항목을 맨 앞으로 땡김
        string.insert(0,string.pop())

    for i in range(len(result)):
        result[i]=int("".join(result[i]),16)

    result.sort(reverse=True)

    print("#"+str(test_case)+" "+str(result[k-1]))