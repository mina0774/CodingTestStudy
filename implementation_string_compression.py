def solution(s):
    answer=0
    LENGTH=len(s)
    # result 값이 될 수 있는 후보를 담는 배열
    cand=[LENGTH]

    for size in range(1,LENGTH):
        # 압축한 단어를 저장할 배열
        compress_string=''

        # s를 지정 개수 단위만큼 쪼개어 만들어진 단어 배열
        splited=[s[i:i+size] for i in range(0,LENGTH,size)]

        # 개수 단위만큼 쪼개진 배열을 압축하여 압축 단어 만들기
        count=1
        for j in range(1,len(splited)):
            prev, cur=splited[j-1],splited[j]

            if prev==cur:
                count+=1
            else:
                if count>1:
                    compress_string+=str(count)+prev
                else:
                    compress_string+=prev
                count=1
        # splited에서 쪼개진 문자열들을 조합할 때 마지막 문자열 위의 for문에서 처리가 안되므로 여기서 처리해줘야함
        if count > 1:
            compress_string += str(count) + splited[-1]
        else:
            compress_string += splited[-1]

        cand.append(len(compress_string))

    answer=min(cand)

    return answer

print(solution('ababcdcdababcdcd'))