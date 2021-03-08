# 구현 문제
# 기둥,보 설치 (2020 카카오 신입 공채)

# 2차원 가상 벽면에 기둥,보 설치 (길이 1)
# 기둥 => 바닥 위 or 보의 한쪽 끝부분 위 or 다른 기둥 위
# 보 => 한쪽 끝부분이 기둥 위 or 양쪽 끝 부분이 다른 보와 동시에 연결

# 2차원 벽면 n*n 크기의 정사각 격자 형태

# build frame은 [x,y,a,b]의 형태
# x,y는 기둥,보를 설치 또는 삭제할 교차점의 좌표 [가로 좌표, 세로 좌표]
# a는 구조물의 종류 0-기둥 1-보
# b는 구조물을 설치할지, 삭제할지 0-삭제 1-설치

# 최종 구조물의 상태를 [x,y,a] 형태의 배열로 반환 / 1) x좌표를 기준으로 오름차순 정렬 2) y좌표를 기준으로 오름차순 정렬

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0: # 설치된 것이 '기둥'인 경우
            # 기둥의 위치가 '바닥 위' '보의 한쪽 끝부분 위' '다른 기둥 위'라면 정상
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif stuff==1: # 설치된 것이 '보'인 경우
            # 보가 '한쪽 끝 부분이 기둥 위' '양쪽 끝 부분이 다른 보와 동시에 연결'라면 정상
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate=frame
        if operate==0: # 삭제하는 경우
            # 일단 삭제
            answer.remove([x,y,stuff])
            # 불가능하다면 다시 설치
            if not possible(answer):
                answer.append([x,y,stuff])
        elif operate==1: # 설치하는 경우
            # 일단 설치
            answer.append([x,y,stuff])
            # 불가능하다면 다시 삭제
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))