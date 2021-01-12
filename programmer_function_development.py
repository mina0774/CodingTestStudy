'''
93 30 55 / 1 30 5 일때
time = 7 라면

93 + 7*1 >= 100
93 / 1 pop
count +=1 // 현재 1

30 + 7*30 >= 100
30 / 30 pop
count +=1  // 현재 2

55+ 5*7 < 100
else 문으로 들어감
현재 count 2니까 answer 배열에 앞선 완료 작업 개수를 넣어줌, count=0으로 변경
그 후 time 증가시킴

그리고 55 + 9*5 >=100 이 됨
55 / 5 pop
count +=1 // 현재 1
'''

def solution(progresses,speeds):
    answer=[]

    time=0
    count=0

    while len(progresses)>0:
        # 만약 스택에 제일 top에 있는 값이 현재의 시간 시점에서 100퍼센트 이상으로 달성되면,
        # 작업이 끝났으므로 스택에서 값을 pop해주고, count를 1 증가시킴
        if(progresses[0]+time*speeds[0]>=100):
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        # 현재 시점에서 100퍼센트 이상이 아닐 때에는 시간을 1 증가시킴
        # 단, count의 값이 0보다 클 경우,
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    # 마지막 count의 개수는 append가 되지 않았으므로
    answer.append(count)

    return answer

print(solution([93,30,55],[1,30,5]))
