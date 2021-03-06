import sys

# 데이터의 개수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 알고리즘을 고려해보아야 함
# 또한 입력 데이터의 개수가 많은 문제에서 input() 함수를 사용하면 동작 속도가 느리기 때문에
# 시간 초과로 오답 판정을 받을 수 있음
# 그러므로 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있음
# rstrip()을 꼭 함께 사용해주어야함
# 왜냐하면 readline()으로 입력 시 엔터가 줄바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야함
input_data=sys.stdin.readline().rstrip()
print(input_data)