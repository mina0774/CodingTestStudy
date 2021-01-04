def solution(priorities, location):
    answer = 0

    index_array = [i for i in range(len(priorities))]  # 문서의 인덱스 값을 저장
    priority_array = priorities.copy()  # 우선순위 배열을 복사

    i = 0
    while True:
        # 현재의 문서보다 나머지 대기목록에서 중요도가 높은 문서가 있을 때
        if priority_array[i] < max(priority_array[i + 1:]):
            # 현재의 인덱스를 대기목록의 맨 뒤로 보내줌 
            index_array.append(index_array.pop(i))
            # 현재의 우선순위를 대기목록의 맨 뒤로 보내줌
            priority_array.append(priority_array.pop(i))
        # 현재 문서가 중요도가 가장 높은 문서일 때 다음 인덱스로 넘어감
        else:
            i = i + 1

        # 우선순위 array가 완전히 정렬되었을 경우 반복문을 빠져나감
        if priority_array == sorted(priorities, reverse=True):
            break

    # 인덱스 배열에서 원하는 대기 문서를 찾아서 그에 해당하는 순서를 반환
    return index_array.index(location) + 1

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))