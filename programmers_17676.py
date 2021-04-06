# [1차] 추석 트래픽 (구현)

def isIn(start,times):
    # 특정 시간 start가 주어졌을 때, 몇 개의 시간이 있는가?
    ret=0
    end=start+1000-1
    for time in times:
        if start<=time[1] and end>=time[0]:
            ret+=1
    return ret


def solution(lines):
    times=[]
    ret=0
    for line in lines:
        p=line.split(' ')
        end=p[1].split(':')
        end=int(end[0])*3600*1000+int(end[1])*60*1000+float(end[2])*1000
        start=end-(float(p[2][:-1])*1000)+1
        times.append((start,end))

    for time in times:
        start,end=time
        ret = max(isIn(start,times),ret)
        ret = max(isIn(end,times), ret)

    return ret

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))