def solution(numbers):
    answer=''

    # 정수가 담겨있는 배열을 문자열이 담겨있는 배열로 변경해줌
    num=list(map(str,numbers))

    # 람다를 이용하여 numbers에 들어가는 숫자가 1000 이하이므로
    # x를 3번만큼 반복하여 3자리수로 맞춘 뒤에 비교하겠다는 의미
    # 가장 큰 수를 만들어야하니까 내림차순으로 정렬
    # 문제 예시에서 666 101010 222 이렇게 만들어지니까
    # 아스키코드로 변환했을 때 첫째자리의 순으로 6 > 2 > 10 으로 수를 비교
    num.sort(key= lambda x : x*3, reverse=True)

    # 모든 값이 0일 때를 처리하기 위해 int로 변환했다가 str로 변환해줌
    answer = str(int(''.join(num)))

    return answer

print(solution([6, 10, 2]))