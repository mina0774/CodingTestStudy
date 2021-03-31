# N으로 표현 (DP)

'''
result = 1일 때 만들 수 있는 숫자
5
result = 2일 때 만들 수 있는 숫자
55
10(5+5) 25(5*5) 1(5/5) 0(5-5)
result = 3일 때 만들 수 있는 숫자
15((5+5)+5) 5((5+5)-5) 2((5+5)/5) 50((5+5)*5)
30((5*5)+5) 20((5*5)-5) 5((5*5)/5) 125((5*5)*5)
.
.
.
'''

def solution(N,number):
    # 조합으로 나올 수 있는 숫자들을 게속 append
    possible_set=[0,[N]]
    # 주어진 숫자 number와 사용해야하는 숫자 N이 같으면 1을 return
    if N==number:
        return 1

    for i in range(2,9):
        case_set=[]
        # 같은 숫자 반복되는 것 추가
        basic_num=int(str(N)*i)
        case_set.append(basic_num)

        for i_half in range(1,i//2+1):
            for x in possible_set[i_half]:
                for y in possible_set[i-i_half]:
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y!=0:
                        case_set.append(x/y)
                    if x!=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
        possible_set.append(case_set)
    return -1

print(solution(2,11))
