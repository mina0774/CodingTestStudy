def solution(skill,skill_trees):
    answer = 0

    # 먼저 스킬트리에서 스킬을 하나씩 꺼내어 반복~
    for skills in skill_trees:
        # 배워야할 스킬 순서를 담은 문자열을 리스트로 변환해줌
        skill_list = list(skill)

        ### 여기서 내가 몰랐던 것 ###
        # python에는 for-else문이 있는데, for문이 중간에 break 등으로 끊기지 않고
        # 끝까지 수행되었을 때 수행하는 코드임

        # 그리고 꺼낸 스킬들의 알파벳을 하나씩 읽어줌
        for s in skills:
            # 그 알파벳이 배워야할 스킬 순서에 담긴 문자열이라면
            if s in skill:
                # 배워야할 스킬 순서대로 스킬을 배워야하므로
                # skill_list의 첫번째 원소를 pop해주어서 비교해주어
                # 순서가 같은지 확인해줘야함
                # 만약 순서가 같지 않다면, 그 스킬은 불가능한 스킬트리이므로 반복문을 빠져나감
                if s != skill_list.pop(0):
                    break
        # for문이 break로 끊기지 않고 끝까지 잘 수행되었을 경우
        else:
            answer += 1

    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))