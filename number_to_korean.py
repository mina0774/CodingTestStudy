# 한화/ICT 기출
# 숫자를 한글로 읽어보기
# divmod( n - 나눠질 값, 10 - 나누는 값 )의 결과값은 몫과 나머지
# ''.join(result[::-1]) => list를 문자열로 변환

def read_number(n):

    units=['','십','백','천','만']
    nums=['일','이','삼','사','오','육','칠','팔','구']

    result=[]

    if n==0:
         return '영'

    i=0
    while n>0:
        n,r=divmod(n,10)
        if r>0:
            if r==1 and i!=0:
                result.append(units[i])
            else:
                result.append(nums[r-1]+units[i])
        i+=1

    return ''.join(result[::-1])

print(read_number(521))