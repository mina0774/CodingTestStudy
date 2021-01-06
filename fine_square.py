from math import gcd


def solution(w, h):
    answer = 1
    # 너비와 높이의 최대공약수를 구하고
    gcd_num = gcd(w, h)
    # 최대공약수만큼 대각선이 지나가는 작은 사각형의 조각이 반복되는 것을 알 수 있음
    # 그리고 작은 사각형의 조각에서 먼저 잘려나간 사각형의 개수를 계산
    w_piece = w / gcd_num
    h_piece = h / gcd_num
    num = w_piece + h_piece - 1
    # 그리고 최대공약수만큼 작은 사각형의 조각이 반복되므로 잘려나간 사각형의 총 개수는 다음과 같음
    num *= gcd_num

    # answer는 전체 사각형의 개수에서 잘려나간 사각형의 총 개수를 빼면 됨
    answer = w * h - num
    return answer

print(solution(8,12))