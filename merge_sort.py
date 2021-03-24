# merge sort (bottom up)

def merge(l, r):
    result=[] # 결과값을 저장할 배열
    i=0
    j=0

    while (i<len(l) and j<len(r)):
        if l[i]<=r[j]: # 왼쪽 배열의 현재 원소가 오른쪽 배열의 현재 원소보다 작거나 같을 때
            result.append(l[i])
            i+=1
        else: # 그 반대일 때
            result.append(r[j])
            j+=1
    # 반복문을 다 돌고 난 후,
    # 왼쪽 배열이 모두 저장이 되었으면, 남은 오른쪽 배열을 결과 배열에 추가해줌
    if i==len(l):
        result=result+r[j:len(r)]
    # 오른쪽 배열이 모두 저장이 되었으면, 남은 왼쪽 배열을 결과 배열에 추가해줌
    if j==len(r):
        result=result+l[i:len(l)]
    return result

def merge_sort(result):
    # 더 이상 분할되지 않는 단위라면
    if len(result)<=1:
        return result
    # 분할하기
    mid=len(result)//2
    l=merge_sort(result[0:mid])
    r=merge_sort(result[mid:len(result)])

    return merge(l,r)

print(merge_sort([5,2,3,1,8,7,9,4,6,10]))


