
def solution(tickets):
    answer = []
    air = {}
    for i in tickets:
        if i[0] not in air.keys():
            air[i[0]] = [i[1]]
        else:
            air[i[0]] += [i[1]]
    for key in air:
        air[key].sort(reverse=True)

    route = ['ICN']

    while route:
        i = route[-1]
        if i not in air or len(air[i]) == 0:
            answer.append(route.pop())
        else:
            route.append(air[i][-1])
            air[i].pop()
        print(air)
        print(route)
    answer.reverse()

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))